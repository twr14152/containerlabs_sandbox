# Adding/upgrading image locally or in docker/containerlab

Option 1 - Add an image from source locally to your machine
 - Follow steps 1, 2, 3

Option 2 - Docker pull
 - Probably the recommended way to get a new image would be to just use docker pull. 
   - docker pull frrouting/frr:latest (deprocated)
   - docker pull quay.io/frrouting/frr:10.3.1 (new link)
```  
$ docker pull quay.io/frrouting/frr:10.3.1
10.3.1: Pulling from frrouting/frr
Digest: sha256:f90d26a9fd5c14fc5795a73b4254ac88bc3186c45bbeb220a225fb6182de812c
Status: Image is up to date for quay.io/frrouting/frr:10.3.1
quay.io/frrouting/frr:10.3.1
$
```
