function myFunction2() {
    var showtimes = document.querySelector('.dropdown');
    var temp2 = showtimes.options[showtimes.selectedIndex].value;
    var temp = document.querySelector(".dropdown-button-2");
    var html = `<div>
                    <h4>Chọn ghế (các ghế còn trống)</h4>
                    {% for i in x %}
                        {% for ti in tickets %}
                            {% if ti.showtimes.id == ${temp2} %}
                                {% if i != ti.seat_number %}
                                <button>{{ ti.seat_number }}</button>
                                {% endif %}
                            {% endif %}
                        {% endfor %}
                    {% endfor %}
                </div>
                <p class="price-ticket">Giá vé: </p>`;
    temp.innerHTML = html;
}