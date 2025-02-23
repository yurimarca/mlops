After finishing the lesson, I would advise to remove from your local conda all temporary environments created while running `mlflow`.
This can be achieved using the following command on Linux Bash:

```sh
conda env list | awk '{print $1}' | grep "mlflow-" | xargs -I {} conda env remove -n {}
```

You can test if it is not going to remove undesired environments prior to running the code above.

```sh
conda env list | awk '{print $1}' | grep "mlflow-"
```
