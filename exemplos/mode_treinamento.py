model.fit(train_images, train_labels, epochs=10, validation_data=(val_images, val_labels))

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Acurácia do modelo nos dados de teste: {test_acc}')
