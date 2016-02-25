/**
 * Created by Abdulrahman Alotaibi
 */
(function(datapoints){
    if (datapoints == undefined || datapoints.length == 0){
        var elem = document.getElementById('canvas');
        elem.innerHTML = "<br/><p>No Data was found</p>";
        return;
    }
        var formatDate = d3.time.format("%Y-%m-%dT%H:%M:%SZ");

        var margin = {top: 50, right: 20, bottom: 30, left: 80},
            width = 960 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        var x = d3.time.scale()
            .range([0, width]);

        var y = d3.scale.linear()
            .range([height, 0]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left");

        var line = d3.svg.line()
            .x(function(d) { return x(d.date); })
            .y(function(d) { return y(d.close); });

        var svg = d3.select("#canvas").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        var data = datapoints.map(function(d) {
            var date = formatDate.parse(d.collected_at.replace(/\.[0-9]+/, ''));
            return {
            date: date,
            close: d.data,
            };
        });

        x.domain(d3.extent(data, function(d) { return d.date; }));
        y.domain(d3.extent(data, function(d) { return d.close; }));

        svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

        svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Temperature");

        svg.append("path")
        .datum(data)
        .attr("class", "line")
        .attr("d", line);
})(datapoints);
