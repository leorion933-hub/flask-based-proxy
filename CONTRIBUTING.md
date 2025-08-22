# 🤝 Contributing to Template Flask App

First off, thank you for considering contributing to this project! Your support and involvement are greatly appreciated. Whether you're fixing bugs, adding features, improving documentation, or suggesting enhancements, your contributions make a difference.

## 📋 Table of Contents

* [Getting Started](#-getting-started)
* [How to Contribute](#-how-to-contribute)
* [Pull Request Guidelines](#-pull-request-guidelines)
* [Reporting Issues](#-reporting-issues)
* [License](#-license)

---

## 🛠️ Getting Started

To set up the project locally:

1. **Fork the repository**: Click the "Fork" button at the top right of the repository page.

2. **Clone your fork**:

   ```bash
   git clone https://github.com/your-username/template-flask-app.git
   cd template-flask-app
   ```

3. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:

   * Copy the example environment file:

     ```bash
     cp .env.example .env
     ```
   * Update `.env` with your configuration.

6. **Run the application**:

   ```bash
   python autoapp.py
   ```

---

## 🧩 How to Contribute

We welcome contributions in various forms:

* **Bug Reports**: If you find a bug, please [open an issue](https://github.com/digitalocean/template-flask-app/issues) with detailed information.

* **Feature Requests**: Have an idea for a new feature? [Open an issue](https://github.com/digitalocean/template-flask-app/issues) to discuss it.

* **Code Contributions**: Ready to write some code? Awesome! Please follow the steps below.

---

## ✅ Pull Request Guidelines

To ensure a smooth collaboration:

1. **Fork the repository** and create your branch from `main`:

   ```bash
   git checkout -b your-feature-name
   ```

2. **Make your changes** and ensure the application runs correctly.

3. **Write tests** for your changes if applicable.

4. **Run tests** to ensure everything works:

   ```bash
   pytest
   ```

5. **Commit your changes** with clear and descriptive messages.

6. **Push to your fork** and submit a pull request:

   ```bash
   git push origin your-feature-name
   ```

7. **Fill out the PR template** and link any related issues.

8. **Be responsive** to any feedback or requested changes.

---

## 🐞 Reporting Issues

If you encounter any issues:

1. **Search existing issues** to avoid duplicates.

2. **Open a new issue** with a clear title and detailed description.

3. **Include steps to reproduce**, expected behavior, and screenshots if applicable.

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).

---

Thank you for being a part of this project! Your contributions help make it better for everyone. Let's build something great together! 🚀
