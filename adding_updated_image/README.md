# Adding/upgrading image in docker/containerlab

Option 1 - Add an image from source locally
 - This works but it can bring issues if you go to the latest and greatest. So docker pull image may be preferrable.
 - To pull an image locally from source follow steps 1, 2, 3.
 - I found this method to be buggy so with that for now I will resort to option 2 below.

Option 2 - Docker pull
 - Probably the recommended way to get a new image would be to just use docker pull. 
   - docker pull frrouting/frr:latest

