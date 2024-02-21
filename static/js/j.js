

const add_cart = (product_id) => {
    fetch(`http://localhost:8000/add_cart`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            product_id: product_id,
        })
    }).then(rsp => rsp.json()).then(response => {
        console.log(response)
    })
}


const delete_wishlist = (id) => {
            fetch('http://localhost:8000/delete_wishlist', {
                method: 'DELETE',
                headers:{
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    product_id: id,
                })
            }).then(rsp=>rsp.json()).then(response=>{
                document.getElementById(`product_${id}`)
                console.log(response)
            })
        }





