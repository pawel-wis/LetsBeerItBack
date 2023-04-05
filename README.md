# LetsBeerItBack
Still under construction.
## Docker
Only for development purposes.
### Docker image build
``` bash
docker build -t image_name .
```
### Docker container run
``` bash
docker run -d -p 8000:8000 --network="host" image_id
```
