document.addEventListener('DOMContentLoaded', function () {
    const quantityInputs = document.querySelectorAll('.quantity-input');
    const summarySubtotal = document.querySelector('.summary-item.subtotal .price');
    const summaryTotal = document.querySelector('.summary-item.total .price');
    const removeButtons = document.querySelectorAll('.remove-product');

    function updateCartTotal() {
        let subtotal = 0;
        quantityInputs.forEach(input => {
            const quantity = parseInt(input.value);
            const productRow = input.closest('.product');
            const priceElement = productRow.querySelector('.price span');
            const unitPrice = parseFloat(priceElement.dataset.unitPrice);
            const totalPrice = quantity * unitPrice;
            console.log(`Quantity: ${quantity}, Unit Price: ${unitPrice}, Total Price: ${totalPrice}`);
            priceElement.textContent = `$${totalPrice.toFixed(2)}`;
            subtotal += totalPrice;
        });
        console.log(`Subtotal: ${subtotal}`);
        summarySubtotal.textContent = `$${subtotal.toFixed(2)}`;
        summaryTotal.textContent = `$${subtotal.toFixed(2)}`;
    }

    function removeProduct(event) {
        const buttonClicked = event.target;
        const productRow = buttonClicked.closest('.product');
        productRow.remove();
        updateCartTotal();
    }

    quantityInputs.forEach(input => {
        input.addEventListener('change', function () {
            if (isNaN(input.value) || input.value <= 0) {
                input.value = 1;
            }
            updateCartTotal();
        });
    });

    removeButtons.forEach(button => {
        button.addEventListener('click', removeProduct);
    });

    updateCartTotal();
});
