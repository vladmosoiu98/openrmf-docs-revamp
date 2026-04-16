============
Contributing
============

OpenRMF OSS welcomes contributions from the community. This page outlines the
process for submitting changes.

Getting Started
===============

1. Identify the repository for your change (see :doc:`repository-map`).
2. Fork the repository on GitHub.
3. Clone your fork locally.
4. Create a feature branch from ``master``.
5. Make your changes.
6. Test your changes (see :doc:`testing`).
7. Commit with a clear, descriptive message.
8. Push to your fork and open a Pull Request against the upstream ``master`` branch.

Code Style
==========

- C# services follow standard .NET naming conventions (PascalCase for public
  members, camelCase for local variables).
- Use consistent indentation (4 spaces for C#, 2 spaces for JavaScript/HTML/CSS).
- Keep methods focused and reasonably sized.
- Add XML documentation comments to public API methods.

Commit Messages
===============

Write clear commit messages that describe the "what" and "why" of the change:

- **Good**: ``Add NIST 800-53 Rev 5 control mapping for AC-2 sub-controls``
- **Bad**: ``Fixed stuff``

Issues and Bug Reports
======================

Use the GitHub Issues tab on the relevant repository to report bugs or request
features. Include:

- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- OpenRMF version and deployment method (Docker Compose, Kubernetes)
- Browser and OS information (for frontend issues)
- Relevant log output

License
=======

By contributing to OpenRMF OSS, you agree that your contributions will be licensed
under the GPL-3.0 license.

Community
=========

- **GitHub**: `github.com/Cingulara <https://github.com/Cingulara>`_
- **Slack**: Community Slack channel (link available on openrmf.io)
- **Website**: `openrmf.io <https://www.openrmf.io/>`_
