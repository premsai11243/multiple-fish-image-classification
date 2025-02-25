
# Multiclass Fish Image Classification

## 📌 Import Necessary Libraries
Click on the library names to visit their official documentation:

- [pandas](https://pandas.pydata.org)
- [numpy](https://numpy.org)
- [TensorFlow](https://www.tensorflow.org)
- [os (Python Documentation)](https://docs.python.org/3/library/os.html)
- [joblib](https://joblib.readthedocs.io)

---

## 🚀 Steps for CNN Model Training and Deployment
1. **Load the data** from the training data file.
2. **Check the shape of the data**: Expected shape `(256,256,3)`.
3. **Check the bit depth** for rescaling the image.
4. **Data Augmentation** for both training and validation data.
5. **Load the data** from the directory for both training and validation.
6. **Build the model** using TensorFlow Keras `Sequential()`.
7. **Compile the model** for training:
   - **Loss Function** → Minimization target.
   - **Optimizer** → Weight update mechanism.
   - **Metrics** → Performance evaluation.
8. **Train the model**.
9. **Make predictions** on test data.
10. **Evaluate the model** with test data.
11. **Classification Report**:

```plaintext
Test Accuracy: 0.9049
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
Weighted Avg: 0.93   0.92      0.92      3187



[Watch the demo](https://github.com/user-attachments/assets/25e51496-e8a8-4acb-9dff-b0609621e31c)





