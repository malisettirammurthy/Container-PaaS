docker build -t rammurthymalisetti/testimage:0.1 -f new.Dockerfile .
echo $?


docker push rammurthymalisetti/testimage:0.1
echo $?
