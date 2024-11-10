from diagrams import Diagram, Cluster
from diagrams.k8s.compute import Pod, StatefulSet
from diagrams.k8s.network import Service, Ingress
from diagrams.k8s.storage import PV, PVC
from diagrams.k8s.group import NS
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server
from diagrams.onprem.container import K3S
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
from diagrams.generic.network import Router, Subnet
from diagrams.generic.device import Mobile, Tablet
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Client
from diagrams.generic.network import Switch

with Diagram("Core Service Architecture", show=True):
    with Cluster("Internet"):
        internet = Rack("Cloud Compute")

        with Cluster("Device Layer"):
            with Cluster("Zigbee/Zywave"):
                zz = [Switch(f"IOT Device {i + 1}") for i in range(0,2)]

            with Cluster("WIFI"):
                router = Router("Home WIFI Router")
                local_subnet = Subnet("Local Subnets: 10.0.0.1/24")

                internet >> router
                router >> local_subnet

                with Cluster("Network Host: eg. 10.0.0.x"):
                    
                    mobile_devices = [Mobile(f"Mobile Device {i + 1}") for i in range(0,2)]
                    host = Server("localhost:8089")
                    clients = [Client(f"Compute Device {i + 1}") for i in range(0,2)]

                    local_subnet >> mobile_devices
                    local_subnet >> clients
                    local_subnet >> host
                    zz >> host

                    with Cluster("Docker"):
                        node_port = Ingress("NodePort:32000")
                        host >> node_port

                        with Cluster("K3s Cluster"):
                            with Cluster("K3s Agent/Node"):
                                with Cluster("Namespace: home-core"):
                                    ha_service = Service("home-assistant-service 80:32000")
                                    home_assistant = Pod("home-assistant:8123")
                                    hastorage = PV("HA -Persistent Volume")
                                    hapvc = PVC("HA- Persistent Volume Claim")
                                    ha_service - home_assistant - hapvc - hastorage
                                    host >> node_port >> ha_service
                            with Cluster("K3s Server/Control Plane"):
                                NS("kube-system, kube-public, kube-node-lease")

