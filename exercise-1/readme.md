``` Communication between two pods , when the pods are published on different nodes ```
Steps:
 - Build a docker image  and incorporate the image names in pod1, pod2 yml 
 - Create pod1 using pod1.yml
 - Define a service for pod1 of Type ClusterIP and publish it
 - Create pod2 using pod2.yml

Reason to define a ClusterIP:
 - pod1 can be reached from other different pods with in the same cluster using the IP address of pod1.
 - But every time  pod1 is republished or recreated , the pod1 IP address changes. So the other pods will end up with a different   IP address of the pod1 they are trying to reach.
 - To solve this issue Kuberenetes provided a service to defines cluster IP , which is static. So all the pods trying to reach      pod1 can use this ipaddress to reach the pod and the specific port.

Command to use:
 - kubectl get deployments
 - kubectl get svc
 - kubectl get pods 

Test:
use command : Kubectl exec -it <pod2_name> bash ; curl <cluster-ip>:8080