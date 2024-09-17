### Descripción del Script ESPAÑOL:

Este script en Python monitorea bloques de la blockchain de **Ethereum** utilizando una lista de nodos **RPC** y busca transacciones que superen un valor mínimo de **0.01 ETH**. Las direcciones involucradas en estas transacciones se guardan en un archivo de texto (`result.txt`). 

El script tiene mecanismos para alternar entre varios nodos RPC en caso de errores o fallos, garantizando la continuidad del monitoreo. También utiliza procesamiento paralelo para aumentar la eficiencia en la verificación de nuevos bloques.

#### Funcionalidades:

1. **Múltiples Nodos RPC**:
   - El script cuenta con una lista de tres nodos RPC:
     - `https://eth.llamarpc.com`
     - `https://eth-pokt.nodies.app`
     - `https://rpc.ankr.com/eth`
   - Si uno de los nodos falla o rechaza solicitudes, el script cambia automáticamente al siguiente nodo disponible.

2. **Monitoreo Continuo de Nuevos Bloques**:
   - El script monitorea continuamente los bloques más recientes de la red de Ethereum.
   - Por cada nuevo bloque detectado, obtiene todas las transacciones.

3. **Filtrado de Transacciones**:
   - Las transacciones son filtradas por valor, y solo aquellas con un valor mayor a **0.01 ETH** son procesadas.
   - Tanto la dirección de origen (`from`) como la de destino (`to`) de las transacciones que superen este umbral se almacenan.

4. **Almacenamiento de Direcciones**:
   - Las direcciones de las transacciones filtradas se guardan en un archivo de texto (`result.txt`), lo que permite un registro continuo de las transacciones relevantes.

5. **Cambio Automático de Nodo RPC**:
   - Si hay un error al conectarse a un nodo RPC o este deja de funcionar, el script cambia automáticamente al siguiente nodo en la lista, garantizando que la tarea no se detenga.

6. **Uso de Procesamiento Paralelo**:
   - El script utiliza `ThreadPoolExecutor` para ejecutar tareas en paralelo, lo que mejora la eficiencia y permite manejar varias operaciones simultáneamente.

#### Uso del Script:

1. **Ejecución**:
   - El script se ejecuta en Python con la siguiente estructura básica:
     ```bash
     python nombre_del_script.py
     ```
   - Se recomienda ejecutarlo en un entorno que tenga instaladas las librerías necesarias, especialmente `requests`.

2. **Operación**:
   - Una vez iniciado, el script monitoreará los nuevos bloques de Ethereum utilizando los nodos RPC disponibles.
   - En caso de que un nodo falle, el script cambiará automáticamente al siguiente nodo de la lista sin necesidad de intervención del usuario.
   
3. **Resultado**:
   - Las direcciones involucradas en transacciones mayores a **0.01 ETH** se guardarán en un archivo llamado `result.txt`, el cual se actualizará a medida que se procesen más bloques.

#### Consideraciones:

- **Conexión a Internet**: Es esencial tener una conexión a Internet estable para interactuar con los nodos RPC.
- **Dependencias**: Se debe tener instalada la librería `requests` para hacer solicitudes HTTP.
- **Tolerancia a Fallos**: El script está diseñado para ser resiliente a fallos de conexión a nodos RPC y continuará operando utilizando nodos alternativos si se detecta un fallo.


### Script Description: ENGLISH

This Python script monitors blocks of the **Ethereum** blockchain using a list of **RPC** nodes and looks for transactions that exceed a minimum value of **0.01 ETH**. The addresses involved in these transactions are saved in a text file (`result.txt`). 

The script has mechanisms to switch between multiple RPC nodes in case of errors or failures, ensuring continuity of monitoring. It also uses parallel processing to increase efficiency in verifying new blocks.

#### Features:

1. **Multiple RPC Nodes**:
   - The script has a list of three RPC nodes:
     - `https://eth.llamarpc.com`
     - `https://eth-pokt.nodies.app`
     - `https://rpc.ankr.com/eth`
   - If one of the nodes fails or rejects requests, the script automatically switches to the next available node.

2. **Continuous Monitoring of New Blocks**:
   - The script continuously monitors the most recent blocks on the Ethereum network.
   - For each new block detected, you get all the transactions.

3. **Transaction Filtering**:
   - Transactions are filtered by value, and only those with a value greater than **0.01 ETH** are processed.
   - Both the source (`from`) and destination (`to`) addresses of transactions that exceed this threshold are stored.

4. **Address Storage**:
   - The addresses of leaked transactions are saved in a text file (`result.txt`), allowing continuous recording of relevant transactions.

5. **Automatic RPC Node Change**:
   - If there is an error connecting to an RPC node or it stops working, the script automatically switches to the next node in the list, ensuring that the task does not stop.

6. **Use of Parallel Processing**:
   - The script uses `ThreadPoolExecutor` to execute tasks in parallel, which improves efficiency and allows multiple operations to be handled simultaneously.
  #### Script Usage:

1. **Execution**:
   - The script is executed in Python with the following basic structure:
     ```bash
     python script_name.py
     ```
   - It is recommended to run it in an environment that has the necessary libraries installed, especially `requests`.

2. **Operation**:
   - Once started, the script will monitor new Ethereum blocks using the available RPC nodes.
   - In case a node fails, the script will automatically switch to the next node in the list without the need for user intervention.
   
3. **Result**:
   - Addresses involved in transactions greater than **0.01 ETH** will be saved in a file called `result.txt`, which will be updated as more blocks are processed.

#### Considerations:

- **Internet Connection**: It is essential to have a stable Internet connection to interact with RPC nodes.
- **Dependencies**: You must have the `requests` library installed to make HTTP requests.
- **Fault Tolerance**: The script is designed to be resilient to connection failures to RPC nodes and will continue to operate using alternative nodes if a failure is detected.
