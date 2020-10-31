from diagrams import Cluster
from diagrams import Diagram
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.k8s.compute import Deployment
from diagrams.k8s.infra import Master
from diagrams.k8s.infra import Node
from diagrams.onprem.monitoring import Prometheus

with Diagram("Telemetry and Subscription Stack", show=False):

    # Customer cluster
    with Cluster("Customer OpenShift"):
        local_metrics = Prometheus("customer metrics")
        cluster = [Master("master"), Node("worker_1"), Node("worker_2")] >> local_metrics  # noqa: E501

    # Telemeter stack
    with Cluster("Telemeter Stack"):
        store = S3("events store")
        thanos = Prometheus("Thanos")
        push = Deployment("pushgateway")
        push >> thanos

    with Cluster("OpenShift Cluster Manager"):
        ocm_db = RDS("ocm_db")
        ocm = Deployment("ocm_account_mgr")
        ocm - ocm_db

    with Cluster("Subscription Stack"):
        tally = Deployment("tally")
        tally_db = RDS("tally_db")
        tally - tally_db

    local_metrics >> store >> thanos
    ocm >> push
    tally - thanos
