===============
Developer Guide
===============

This section covers everything a developer or contributor needs to work with the
OpenRMF OSS codebase: setting up a local development environment, building services,
running tests, contributing changes, and understanding the repository layout.

OpenRMF is a multi-repository project. Each microservice lives in its own GitHub
repository under the `Cingulara <https://github.com/Cingulara>`_ organization. All
backend services are written in C# targeting .NET Core, while the frontend is
JavaScript/HTML/CSS served by NGINX.

.. toctree::
   :maxdepth: 1

   local-setup
   building
   testing
   contributing
   repository-map
