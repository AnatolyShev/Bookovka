import {$authHost, $host} from "./index";

//Создать свои запросы к своим эндпоинтам на бэке
export const createUser = async (user) => {
    const {data} = await $host.post('api/user', user) //$authHost
    return data
}

export const createType = async (type) => {
    const {data} = await $host.post('api/type', type) //$authHost
    return data
}

export const createBrand = async (brand) => {
    const {data} = await $host.post('api/brand', brand) //$authHost
    return data
}

export const createGoods = async (goods) => {
    const {data} = await $host.post('api/goods', goods) //$authHost
    return data
}

export const createSubtype = async (subtype) => {
    const {data} = await $host.post('api/subtype', subtype) //$authHost
    return data
}

export const createBasket = async (basket) => {
    const {data} = await $host.post('api/basket', basket) //$authHost
    return data
}

export const createBasketGoods = async (basket_goods) => {
    const {data} = await $host.post('api/basket_goods', basket_goods) //$authHost
    return data
}

export const deleteType = async (id) => {
    const {response} = await $host.delete('api/type/' + id) //$authHost
    return response
}

export const deleteSubtype = async (id) => {
    const {response} = await $host.delete('api/subtype/' + id) //$authHost
    return response
}

export const deleteSubtypeCascade = async (id) => {
    const {response} = await $host.delete('api/subtype_cascade/' + id) //$authHost
    return response
}

export const deleteUser = async (user_id) => {
    const {response} = await $host.delete('api/user/' + user_id) //$authHost
    return response
}

export const deleteGoods = async (id) => {
    const {response} = await $host.delete('api/goods/' + id) //$authHost
    return response
}

export const deleteBrand = async (id) => {
    const {response} = await $host.delete('api/brand/' + id) //$authHost
    return response
}

export const deleteBasketGoods = async (id) => {
    const {response} = await $host.delete('api/basket_goods/' + id) //$authHost
    return response
}

export const fetchTypes = async () => {
    const {data} = await $host.get('api/type')
    return data
}

export const fetchSubtypes = async () => {
    const {data} = await $host.get('api/subtype')
    return data
}

export const fetchUsers = async () => {
    const {data} = await $host.get('api/user')
    return data
}

export const fetchGoods = async () => {
    const response = await $host.get('api/goods')
    console.log(response.data)
    return response.data
}

export const fetchBaskets = async () => {
    const {data} = await $host.get('api/basket')
    return data
}

export const fetchBasketsGoods = async () => {
    const {data} = await $host.get('api/basket_goods')
    return data
}

export const fetchBrands = async () => {
    const {data} = await $host.get('api/brand')
    return data
}

export const fetchUserById = async (id) => {
    const {data} = await $host.get('api/user/' + id)
    return data
}

export const fetchTypeById = async (id) => {
    const { data } = await $host.get(`api/type/${id}`);
    return data;
};

export const fetchSubtypeById = async (id) => {
    const { data } = await $host.get(`api/subtype/${id}`);
    return data;
};

export const fetchBrandById = async (id) => {
    const { data } = await $host.get(`api/brand/${id}`);
    return data;
};

export const fetchGoodsById = async (id) => {
    const {data} = await $host.get('api/goods/' + id)
    return data
}

export const fetchBasketById = async (id) => {
    const {data} = await $host.get('api/basket/' + id)
    return data
}

export const fetchBasketGoodsById = async (id) => {
    const {data} = await $host.get('api/basket_goods/' + id)
    return data
}

// export const createCategory = async (category) => {
//     const {data} = await $authHost.post('api/category/', category)
//     return data
// }

// export const deleteCategory = async (id) => {
//     const {response} = await $authHost.delete('api/category/'+ id)
//     return response
// }

// export const fetchCategory = async () => {
//     const {data} = await $host.get('api/category', )
//     return data
// }

// export const fetchCategoryById = async (id) => {
//     const { data } = await $host.get(`api/category/${id}`);
//     return data;
// };

// export const fetchLegal = async () => {
//     const {data} = await $host.get('api/legal', )
//     return data
// }

// export const createLegal = async (legal) => {
//     const {data} = await $host.post('api/legal/new', legal)
//     return data
// }

// export const deleteLegal = async (id) => {
//     const {response} = await $host.post('api/legal/' + id)
//     return response
// }


// export const createProduct = async (product) => {
//     const {data} = await $authHost.post('/api/product/', product)
//     return data
// }

// export const delProduct = async (id) => {
//     const {data} = await $authHost.post('api/product/del/'+ id)
//     return data
// }

// export const fullDeleteProduct = async (id) => {
//     const {response} = await $authHost.delete('api/product/'+ id)
//     return response
// }

// export const setDescription = async (_id, text) => {
//     const {data} = await $authHost.post('api/product/update', _id, text)
//     return data
// }

// export const fetchProducts = async (typeId, brandId, categoryId, page, limit) => {
//     const {data} = await $host.get('api/product/', {params: {
//             typeId, brandId, categoryId, page, limit
//         }})
//     // console.log('Request parameters:', typeId, brandId, categoryId, page, limit);
//     // console.log(data)
//     return data
// }

// export const fetchAllProducts = async () => {
//     const {data} = await $host.get('api/product/all', )
//     return data
// }


// export const fetchOneProduct = async (id) => {
//     const {data} = await $host.get('api/product/'+id)
//     return data
// }

// // ------ Корзина ------- //
// export const addToBasket = async (data) => {
//     const { response } = await $authHost.post('api/basket', data);
//     return response;
// };

// export const deleteFromBasket = async (id) => {
//     const {response} = await $authHost.post('api/basket/delete', {id:id})
//     return response
// }

// export const getBasket = async () => {
//     const {data} = await $authHost.get('api/basket')
//     return data
// }
// // ------ Заказы ------- //
// export const addOrder = async (id, phone, postcode, addressee) => {
//     const {data} = await $host.post('api/order', {
//             id, phone, postcode, addressee
//         })
//     return data
// }

// export const getOrder = async (id) => {
//     const {data} = await $authHost.get('api/order/')
//     return data
// }


// export const getUserOrder = async (id) => {
//     if(!id)id = 0;
//     const {data} = await $authHost.get('api/order/'+id, id)
//     return data
// }

// export const getUserOrderList = async (id) => {
//     if(!id)id = 0;
//     const {data} = await $authHost.get('api/order/'+id, id)
//     return data
// }

// export const updateUserOrder = async (id, status) => {
//     if(!id)id = 0;
//     const {data} = await $authHost.post('api/order/update/'+id, {params:{id, status}})
//     return data
// }



// export const updateAmount = async (_id, _amount) => {
//     const {data} = await $authHost.post('api/product/update/'+_id, {_id, _amount})
//     return data
// }

// export const deleteOrder = async (id) => {
//     const {response} = await $authHost.delete('api/order/' + id);
//     return response;
// };