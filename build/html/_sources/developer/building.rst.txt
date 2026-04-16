==================
Building Services
==================

Each OpenRMF microservice can be built as a .NET application or as a Docker
container image.

Building with .NET
==================

From the ``src/`` directory of any service::

   dotnet restore
   dotnet build

This compiles the service and produces output in ``bin/Debug/``.

For a release build::

   dotnet publish -c Release -o ./publish

Building Docker Images
======================

Each repository includes a ``Dockerfile`` and a ``Makefile`` for container builds.

**Using Make:**

::

   make build       # Builds the Docker image with the default tag
   make latest      # Builds and tags as :latest

**Using Docker directly:**

::

   docker build -t cingulara/openrmf-api-read:local .

The Dockerfiles use a multi-stage build pattern:

1. **Build stage**: Uses the .NET SDK image to restore, build, and publish the
   application.
2. **Runtime stage**: Uses the lightweight .NET ASP.NET runtime image
   (``mcr.microsoft.com/dotnet/aspnet``) to run the published application.

This keeps the final container image small by excluding build tools and source code.

Building All Services
=====================

To build all services locally, clone each repository and run the build command. A
helper script can automate this::

   #!/bin/bash
   REPOS=(
       openrmf-api-read
       openrmf-api-save
       openrmf-api-upload
       openrmf-api-template
       openrmf-api-scoring
       openrmf-api-controls
       openrmf-api-compliance
       openrmf-api-audit
       openrmf-api-reports
       openrmf-msg-score
       openrmf-msg-reports
       openrmf-msg-system
       openrmf-msg-audit
       openrmf-msg-compliance
       openrmf-msg-controls
       openrmf-msg-template
       openrmf-msg-checklist
       openrmf-web
   )

   for repo in "${REPOS[@]}"; do
       echo "Building $repo..."
       cd "$repo" && make build && cd ..
   done

.. note::

   Building the ``openrmf-web`` image also bundles the Jekyll-generated help
   documentation. Ensure Ruby and Bundler are available if you need to regenerate
   the help content before building.
