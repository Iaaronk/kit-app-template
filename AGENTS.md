Overview
This project aims to develop a virtual try-on platform that allows users to select clothing items and visualize them on animated 3D characters. The platform leverages Character Creator models, integrates animations, and streams the experience through a web-based viewer.
IDM VTON
+2
web.clo-z.app
+2
Outfit Anyone
+2

Project Scope
Character Modeling: Utilize Character Creator to design realistic 3D human models.

Clothing Integration: Implement virtual try-on capabilities, enabling users to select garments and see them fitted on the models.

Animation: Animate the characters to showcase the clothing in motion, enhancing the realism of the try-on experience.

Web Streaming: Stream the interactive experience using the web-viewer-sample, allowing users to access the platform through a web browser.
3d.kalidoface.com
+3
Unreal Engine
+3
Meshy AI
+3

Code Style
Languages: Python and C++

Formatting:

Use Black for Python code formatting.

Adhere to PEP 8 guidelines for Python code.

Follow the Google C++ Style Guide for C++ code.

Naming Conventions:

Use snake_case for Python variables and functions.

Use PascalCase for class names.

Use SCREAMING_SNAKE_CASE for constants.
Reallusion
+3
Kolors Virtual
+3
giomhbyrj.blob.core.windows.net
+3

Project Structure
.vscode/: Visual Studio Code configuration files.

readme-assets/: Assets for README and documentation.

source/: Source code for applications and extensions.

templates/: Template applications and extensions.

tools/: Utility scripts and tools for development.

.editorconfig: Editor configuration to maintain consistent coding styles.

premake5.lua: Build configuration script.

repo.toml: Top-level configuration for repository tools.

repo_tools.toml: Configuration for local repository-specific tools.
icrea.xyz

Build and Launch
Building the Project:

On Windows:

bash
Copy
Edit
.\repo.bat build
On Linux:

bash
Copy
Edit
./repo.sh build
Launching the Application:

On Windows:

bash
Copy
Edit
.\repo.bat launch
On Linux:

bash
Copy
Edit
./repo.sh launch
Creating a New Application from Template:

On Windows:

bash
Copy
Edit
.\repo.bat template new
On Linux:

bash
Copy
Edit
./repo.sh template new
Follow the prompts to configure your new application.

Testing
Python:

Use pytest for writing and running tests.

Place test files in the tests/ directory, mirroring the structure of the source/ directory.

C++:

Use Google Test framework for unit tests.

Place test files in the tests/ directory, following the structure of the source/ directory.

Commit Messages
Follow the Conventional Commits specification.

Examples:

feat: integrate virtual try-on functionality

fix: resolve animation playback issue

docs: update AGENTS.md with project scope

Pull Requests
Ensure all linting and tests pass before submitting a PR.

Provide a clear description of the changes made.

Reference any related issues in the PR description.

Environment Setup
Operating System: Windows 10/11 or Linux (Ubuntu 22.04 or newer)

GPU: NVIDIA RTX capable GPU (RTX 3070 or better recommended)

Driver: Minimum version 537.58

Required Software:

Git

Git LFS

Microsoft Visual Studio 2019 or 2022 with Desktop development with C++ workload (Windows)

Windows SDK (Windows)

build-essential package (Linux)

Docker and NVIDIA Container Toolkit (Linux, optional for containerized development)

Visual Studio Code or preferred IDE
giomhbyrj.blob.core.windows.net
+19
Kritikal Solutions
+19
Reallusion
+19

Additional Resources
Omniverse Kit SDK Companion Tutorial

Omniverse Kit App Template Documentation
