
<h2>multiclassFish  image classification</h2>
<h3>import necessary libraries</h3>
<a href="https://pandas.pydata.org">Click Here</a>
<a href="https://numpy.org">Click Here</a>
<a href="https://www.tensorflow.org">Click Here</a>
<a href=" https://docs.python.org/3/library/os.html">Click Here</a>
<a href="https://joblib.readthedocs.io">Click Here</a>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CNN Model Training Steps</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h2 { color: #2c3e50; }
        pre { background: #ecf0f1; padding: 10px; border-radius: 5px; overflow-x: auto; }
        code { font-family: Consolas, monospace; }
    </style>
</head>
<body>
    <h2>Steps for CNN Model Training and Deployment</h2>
    <ol>
        <li><strong>Load the data</strong> from the training data file.</li>
        <li><strong>Check the shape of data</strong>: Expected shape (256,256,3)</li>
        <li><strong>Check the bit depth</strong> for rescaling the image.</li>
        <li><strong>Data Augmentation</strong> for both training and validation data.</li>
        <li><strong>Load the data</strong> from the directory for both training and validation.</li>
        <li><strong>Build the model</strong> using TensorFlow Keras Sequential.</li>
        <li><strong>Compile the model</strong> for training:
            <ul>
                <li>Loss Function → Minimization target.</li>
                <li>Optimizer → Weight update mechanism.</li>
                <li>Metrics → Performance evaluation.</li>
            </ul>
        </li>
        <li><strong>Train the model</strong>.</li>
        <li><strong>Make predictions</strong> on test data.</li>
        <li><strong>Evaluate the model</strong> with test data.</li>
        <li><strong>Classification Report</strong>:</li>
    </ol>
    <pre><code>Test Accuracy: 0.9049
Test Loss: 0.2485

Precision    Recall  F1-score   Support
0       0.97      0.98      0.98       516
1       0.15      0.33      0.21         6
2       0.96      0.97      0.97       295
3       0.94      0.69      0.80       418
4       0.99      0.94      0.97       301
5       0.90      1.00      0.95       263
6       0.79      0.97      0.88       223
7       0.87      0.93      0.90       304
8       0.96      0.99      0.97       279
9       0.97      0.88      0.92       323
10      0.87      0.98      0.92       259

Accuracy: 0.92
Macro Avg: 0.85      0.88      0.86      3187
Weighted Avg: 0.93   0.92      0.92      3187</code></pre>
    <ol start="12">
        <li><strong>Deploy the model</strong> using a Streamlit web application.</li
    </ol>
</body>
</html>




https://github.com/user-attachments/assets/ec81ae64-d954-4d5d-83ff-7d78c60a1f29


