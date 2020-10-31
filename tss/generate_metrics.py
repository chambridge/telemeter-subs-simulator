from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import push_to_gateway

from .config import Config
from .config import REGISTRY


# node_role_os_version_machine:cpu_capacity_cores:sum{
# _id="000bfac0-e510-4c41-8734-d3345b3b5389",
# label_kubernetes_io_arch="amd64",
# label_node_hyperthread_enabled="true",
# label_node_openshift_io_os_id="rhcos",
# label_node_role_kubernetes_io_master="true",
# prometheus="openshift-monitoring/k8s",
# receive="true",
# tenant_id="FB870BF3-9F3A-44FF-9BF7-D7A047A52F43"}
CPU_CAPACITY_CORES_DICT = {
    "name": "node_role_os_version_machine:cpu_capacity_cores:sum",
    "documentation": "The total number of CPU cores in the cluster labeled by master and/or infra node role, os, architecture, and hyperthreading state.",  # noqa: E501
    "labelnames": [
        "_id",
        "label_kubernetes_io_arch",
        "label_node_hyperthread_enabled",
        "label_node_openshift_io_os_id",
        "label_node_role_kubernetes_io_master",
        "tenant_id",
    ],
    "registry": REGISTRY,
}
CPU_CAPACITY_CORES = Gauge(**CPU_CAPACITY_CORES_DICT)

# cluster:sub_attr{account="RHaccount",
# _id="000bfac0-e510-4c41-8734-d3345b3b5389",
# uom="cores", service_level="L1-L3",
# sla="premium", production_status="production"}
CLUSTER_SUB_ATTR_DICT = {
    "name": "cluster:sub_attr",
    "documentation": "The definition of the cluster's subscription attributes.",  # noqa: E501
    "labelnames": ["account", "_id", "uom", "service_level", "sla", "production_status"],  # noqa: E501
    "registry": REGISTRY,
}
CLUSTER_SUB_ATTR = Counter(**CLUSTER_SUB_ATTR_DICT)


def generate():
    """Generates metrics for simulation."""

    cluster_one_master = {
        "_id": "000bfac0-e510-4c41-8734-d3345b3b5389",
        "label_kubernetes_io_arch": "amd64",
        "label_node_hyperthread_enabled": "true",
        "label_node_openshift_io_os_id": "rhcos",
        "label_node_role_kubernetes_io_master": "true",
        "tenant_id": "FB870BF3-9F3A-44FF-9BF7-D7A047A52F43",
    }
    CPU_CAPACITY_CORES.labels(**cluster_one_master).set(6)
    cluster_one_worker = {
        "_id": "000bfac0-e510-4c41-8734-d3345b3b5389",
        "label_kubernetes_io_arch": "amd64",
        "label_node_hyperthread_enabled": "true",
        "label_node_openshift_io_os_id": "rhcos",
        "label_node_role_kubernetes_io_master": "false",
        "tenant_id": "FB870BF3-9F3A-44FF-9BF7-D7A047A52F43",
    }
    CPU_CAPACITY_CORES.labels(**cluster_one_worker).set(12)

    cluster_one_subs = {
        "account": "28187121",
        "_id": "000bfac0-e510-4c41-8734-d3345b3b5389",
        "uom": "cores",
        "service_level": "L1-L3",
        "sla": "premium",
        "production_status": "production",
    }
    CLUSTER_SUB_ATTR.labels(**cluster_one_subs).inc()

    if Config.PROMETHEUS_PUSH_GATEWAY:
        push_to_gateway(Config.PROMETHEUS_PUSH_GATEWAY, job="pendo_metrics", registry=REGISTRY)  # noqa: E501
