const searchName = document.querySelector("#search-name");
const searchCategory = document.querySelector("#search-category");
const searchSubmit = document.querySelector("#search-submit");
const productDataTable = document.querySelector("#product-data");
const loadingOverlay = document.querySelector(".loading-overlay");

const setLoading = (isShow = false) => {
    if (isShow) {
        loadingOverlay.classList.remove("d-none");
    } else {
        loadingOverlay.classList.add("d-none");
    }
};

const getListCategories = async () => {
    try {
        const response = await axios.get("http://localhost:9000/categories");
        const listCategories = response.data;
        return listCategories;
    } catch (error) {
        console.error("Error fetching data:", error);
        return null;
    }
};

const setListCategoriesHtml = (listCategories) => {
    let listCategoriesHtml = `<option value="">---Danh mục---</option>`;
    listCategoriesHtml += listCategories.map((category) => `<option value="${category}">${category}</option>`).join("");
    searchCategory.innerHTML = listCategoriesHtml;
};

const getListProducts = async () => {
    setLoading(true);

    let url = `http://localhost:9000/products?name=${searchName.value}`;
    if (searchCategory) {
        url += `&category=${searchCategory.value}`;
    }

    try {
        const response = await axios.get(url);
        if (response.data.type === "success") {
            const listProducts = response.data.data;
            return listProducts;
        } else {
            console.error("Failed fetching data");
            return null;
        }
    } catch (error) {
        console.error("Error fetching data:", error);
        return null;
    } finally {
        setTimeout(() => setLoading(false), 500);
    }
};

const setListProductsHtml = (listProducts) => {
    const listProductsHtml = listProducts
        .map((product) => {
            return `<tr>
                        <th class="text-center">${product.id}</th>
                        <td class="text-center">
                            <img src="${product.image_url}" alt="${product.name}" class="product-image">
                        </td>
                        <td class="text-center">${product.name}</td>
                        <td class="text-center">${product.category}</td>
                        <td class="text-center">${product.brand}</td>
                        <td class="text-center">${Number(product.price).toLocaleString("vi-VI")}đ</td>
                    </tr>`;
        })
        .join("");
    productDataTable.innerHTML = listProductsHtml;
};

const main = async () => {
    const listCategories = await getListCategories();
    if (listCategories) setListCategoriesHtml(listCategories);

    const listProducts = await getListProducts();
    if (listProducts) setListProductsHtml(listProducts);

    searchSubmit.onclick = async () => {
        const listProducts = await getListProducts();
        if (listProducts) setListProductsHtml(listProducts);
    };
};

main();
