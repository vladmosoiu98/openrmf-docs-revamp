=======
Testing
=======

Each OpenRMF API service repository includes a ``tests/`` directory with unit tests.

Running Unit Tests
==================

From the root of a service repository::

   cd tests
   dotnet test

Or from the repository root::

   dotnet test tests/

Test output includes pass/fail counts and any assertion failure details.

Test Coverage
=============

To generate a test coverage report, use the ``coverlet`` tool::

   dotnet test tests/ /p:CollectCoverage=true /p:CoverageOutputFormat=opencover

Integration Testing
===================

Full integration tests require the complete infrastructure stack running (MongoDB,
NATS, Keycloak). The recommended approach:

1. Start the infrastructure using Docker Compose (see :doc:`local-setup`).
2. Start the service under test locally or in a container.
3. Use tools like ``curl``, Postman, or a test runner to exercise the API endpoints.

For authentication-gated endpoints, obtain a JWT token from Keycloak first::

   TOKEN=$(curl -s -X POST \
       "http://localhost:8080/auth/realms/openrmf/protocol/openid-connect/token" \
       -H "Content-Type: application/x-www-form-urlencoded" \
       -d "grant_type=password&client_id=openrmf&username=admin&password=yourpassword" \
       | jq -r '.access_token')

   curl -H "Authorization: Bearer $TOKEN" http://localhost:8080/api/read/

Testing NATS Messaging
======================

To verify NATS message flows:

1. Use the ``nats`` CLI tool to subscribe to subjects::

      nats sub "openrmf.>"

2. Trigger an action through the API (e.g., upload a checklist).
3. Observe the published messages and subscriber processing in the terminal.

The ``nats`` CLI can be installed from https://github.com/nats-io/natscli.
