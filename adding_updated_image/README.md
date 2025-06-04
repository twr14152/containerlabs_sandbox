# Adding/upgrading image locally or in docker/containerlab

Option 1 - Add an image from source locally to your machine
 - Follow steps 1, 2, 3

Option 2 - Docker pull
 - Probably the recommended way to get a new image would be to just use docker pull. 
   - docker pull frrouting/frr:latest (deprocated)
   - docker pull quay.io/frrouting/frr:10.3.1 (new link)
```  
toddriemenschneider@clab:~$  docker pull quay.io/frrouting/frr:10.3.1
10.3.1: Pulling from frrouting/frr
94e9d8af2201: Pull complete 
73b107cebb87: Pull complete 
3c7be5c74b89: Pull complete 
f16ad5860883: Pull complete 
4f4fb700ef54: Pull complete 
fcb235d44bf7: Pull complete 
95b18daab98c: Pull complete 
Digest: sha256:f90d26a9fd5c14fc5795a73b4254ac88bc3186c45bbeb220a225fb6182de812c
Status: Downloaded newer image for quay.io/frrouting/frr:10.3.1
quay.io/frrouting/frr:10.3.1
toddriemenschneider@clab:~$ 
```
