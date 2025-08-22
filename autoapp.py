import asyncio
from flask import Flask, request, Response, redirect
from playwright.async_api import async_playwright
import yt_dlp

app = Flask(__name__)
cache = {}

@app.route('/')
def index():
    return '''
        <form action="/proxy">
            <input name="url" placeholder="Enter URL" style="width:300px">
            <button type="submit">Go</button>
        </form>
        <form action="/youtube">
            <input name="video" placeholder="YouTube URL" style="width:300px">
            <button type="submit">Stream</button>
        </form>
    '''

@app.route('/proxy')
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return "No URL provided", 400

    if target_url in cache:
        return Response(cache[target_url], mimetype='text/html')

    content = asyncio.run(render_page(target_url))
    if content:
        cache[target_url] = content
        return Response(content, mimetype='text/html')
    else:
        return "Failed to load page", 500

async def render_page(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )
        context = await browser.new_context()
        page = await context.new_page()

        await page.route("**/*", lambda route: route.abort()
                         if route.request.resource_type in ["image", "stylesheet", "font"]
                         else route.continue_())

        try:
            print(f"Rendering: {url}")
            await page.goto(url, wait_until="domcontentloaded", timeout=15000)
            content = await page.content()
            if not content or "<html" not in content.lower():
                print("Empty or invalid content received.")
                content = None
        except Exception as e:
            print(f"Error loading {url}: {e}")
            content = None

        await browser.close()
        return content

@app.route('/youtube')
def youtube():
    video_url = request.args.get('video')
    if not video_url:
        return "No video URL provided", 400

    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True,
        'skip_download': True,
        'forceurl': True,
        'forcejson': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            stream_url = info['url']
            return redirect(stream_url)
    except Exception as e:
        print(f"Error streaming video: {e}")
        return "Failed to stream video", 500
# ✅ Add this to run the app
if __name__ == '__main__':
    app.run(debug=True)
