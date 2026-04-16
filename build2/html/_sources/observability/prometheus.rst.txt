===========
Prometheus
===========

Prometheus collects metrics from all OpenRMF API services and the NATS message
broker. In Docker Compose deployments, Prometheus is bundled and accessible behind
the ``/metrics/`` path on the NGINX proxy.

Metrics Sources
===============

OpenRMF exposes metrics through two mechanisms:

**prometheus-net (.NET Core APIs)**
   Each API service uses the ``prometheus-net`` library to expose standard ASP.NET
   Core metrics at its ``/metrics`` endpoint. These include HTTP request counts,
   response times, error rates, memory usage, and garbage collection statistics.

**NATS Prometheus Exporter**
   A dedicated exporter container (port 7777) scrapes metrics from the NATS server
   and exposes them in Prometheus format. Metrics include message throughput,
   connection counts, subscription counts, and server resource utilization.

**NATS Client Metrics**
   A custom metrics exporter (port 7778) from the
   `nats-client-metrics <https://github.com/Cingulara/nats-client-metrics>`_
   project provides per-client metrics beyond the server-level aggregates.

Scrape Configuration
====================

The default Prometheus configuration scrapes the following targets at 30-second
intervals:

.. list-table::
   :header-rows: 1
   :widths: 35 15 50

   * - Target
     - Port
     - Description
   * - NATS Exporter
     - 7777
     - NATS server metrics
   * - NATS Client Metrics
     - 7778
     - Per-client NATS metrics
   * - openrmf-api-read
     - 8080
     - Read API metrics
   * - openrmf-api-save
     - 8080
     - Save API metrics
   * - openrmf-api-template
     - 8080
     - Template API metrics
   * - openrmf-api-controls
     - 8080
     - Controls API metrics
   * - openrmf-api-compliance
     - 8080
     - Compliance API metrics
   * - openrmf-api-scoring
     - 8080
     - Scoring API metrics
   * - openrmf-api-upload
     - 8080
     - Upload API metrics
   * - openrmf-api-audit
     - 8080
     - Audit API metrics
   * - openrmf-api-reports
     - 8080
     - Reports API metrics

Accessing Prometheus
====================

In Docker Compose deployments, Prometheus is accessible at::

   http://<your-ip>:8080/metrics/prometheus/

For Kubernetes deployments, access depends on your ingress configuration or you may
use your cluster's existing Prometheus instance.

Useful PromQL Queries
=====================

**HTTP request rate by API**::

   rate(http_requests_received_total[5m])

**95th percentile response time**::

   histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

**NATS message throughput**::

   rate(nats_server_msg_total[5m])

For comprehensive PromQL documentation, see the
`Prometheus querying guide <https://prometheus.io/docs/prometheus/latest/querying/basics/>`_.
