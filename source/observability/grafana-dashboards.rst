==================
Grafana Dashboards
==================

Grafana provides visual dashboards for the metrics collected by Prometheus. In Docker
Compose deployments, Grafana is accessible behind the NGINX proxy.

Accessing Grafana
=================

Navigate to::

   http://<your-ip>:8080/metrics/grafana/

Default credentials:

- **Username**: ``admin``
- **Password**: set in the ``.grafana`` configuration file or ``docker-compose.yml``

.. warning::

   Change the default Grafana admin password after initial setup. See
   :doc:`/security/hardening`.

Pre-Configured Dashboards
==========================

OpenRMF ships with several Grafana dashboards. Additional dashboards can be imported
from the Grafana dashboard registry.

ASP.NET Core Default Metrics (Dashboard 10427)
-----------------------------------------------

Tracks runtime performance across all .NET Core API services:

- Memory consumption and allocation rates
- Garbage collection frequency and duration
- Thread pool usage
- HTTP connection counts

API Controller Metrics (Dashboard 10915)
-----------------------------------------

Monitors HTTP endpoint performance at the controller level:

- Request volume by endpoint
- Response time distributions
- Error rates (4xx, 5xx)
- Request throughput trends

NATS Server Metrics (Dashboard 2279)
--------------------------------------

Displays NATS message broker health:

- Message throughput (in/out)
- Active connection counts
- Subscription counts
- Server CPU and memory usage

NATS Client Metrics (Custom)
------------------------------

Per-client metrics from the ``nats-client-metrics`` exporter:

- Messages sent/received per client
- Connection status per client
- Subscription counts per client

Importing Additional Dashboards
================================

1. Navigate to Grafana's dashboard import page.
2. Enter the dashboard ID from `grafana.com/dashboards <https://grafana.com/grafana/dashboards/>`_.
3. Select the Prometheus data source.
4. Click **Import**.

Creating Custom Dashboards
===========================

Custom dashboards can query any metric exposed by the API services or NATS. Common
panels include:

- **Time series**: request rates, response times, message throughput
- **Gauge**: current active connections, queue depth
- **Stat**: total checklist count, system count
- **Table**: top endpoints by error rate

Alerting
========

Grafana supports alerting rules that can notify via email, Slack, or webhook when
metrics exceed thresholds. Common alert scenarios:

- API error rate exceeds 5% over 5 minutes
- NATS message backlog grows beyond a threshold
- MongoDB connection failures detected
- Memory usage exceeds 80% on any service
