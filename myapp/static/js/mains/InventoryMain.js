import { getProductsByFilter } from "../api/GetProductsByFilter.js";
import { renderProducts } from "../ui/RenderProducts.js";
import { pagination_interface_render } from "../ui/Pagination.js";

let currentPage = 1;
let currentFilter = "";

// Função para carregar produtos e atualizar a paginação
async function loadInventory(page = 1, filter = "") {
  try {
    const data = await getProductsByFilter(page, filter);
    renderProducts(data);
    pagination_interface_render(data);
    currentPage = data.current_page;
  } catch (err) {
    console.error("Erro ao carregar produtos:", err);
    document.getElementById("auctions").innerHTML =
      "<p>Erro ao carregar produtos.</p>";
  }
}

// Inicializa o inventário
document.addEventListener("DOMContentLoaded", () => {
  loadInventory();

  // Botões de paginação
  const prevBtn = document.getElementById("prev-page");
  const nextBtn = document.getElementById("next-page");

  if (prevBtn && nextBtn) {
    prevBtn.addEventListener("click", () => {
      if (currentPage > 1) {
        loadInventory(currentPage - 1, currentFilter);
      }
    });

    nextBtn.addEventListener("click", () => {
      loadInventory(currentPage + 1, currentFilter);
    });
  }

  // Filtro de pesquisa (se houver input)
  const filterInput = document.getElementById("filter-input");
  if (filterInput) {
    filterInput.addEventListener("input", (e) => {
      currentFilter = e.target.value;
      loadInventory(1, currentFilter);
    });
  }
});
