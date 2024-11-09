from diagrams import Diagram, Cluster
from diagrams.k8s.compute import Pod, StatefulSet
from diagrams.k8s.network import Service, Ingress
from diagrams.k8s.storage import PV, PVC
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.queue import Kafka
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage

with Diagram("Core Service Architecture", show=True):

    # Define the Kubernetes Cluster
    with Cluster("Kubernetes Cluster"):

        # Core Namespace for Home Automation and Security
        with Cluster("Namespace: home-core"):

            home_assistant = Rack("Home Assistant")
            hastorage = PV("HA -Persistent Volume")
            hapvc = PVC("HA- Persistent Volume Claim")
            home_assistant - hapvc - hastorage

