window.addEventListener(
  'load',
  function () {
    var svgns = 'http://www.w3.org/2000/svg';
    var mapview = document.getElementById('mapview');
    var viewsize = 1000;
    var halfsize = viewsize / 2;

    var sqrtn = function (x, n) {
      for (var k = 0; k < n; k++) {
        x = Math.sqrt(x);
      }
      return x;
    };

    var radius_distribution = function (u) {
      var a = sqrtn(Math.sin(0.5 * Math.PI * u), 2);
      var b = u * u;

      return (a + b*b) / 2;
    };

    var angle_distribution = function (u) {
      var factor = 3 * Math.PI;
      var a = Math.sin(factor * u);
      var b = Math.pow(Math.abs(a), 1.1);
      return u - b / factor;
    };

    var plot = function (x, y, color) {
      var circle = document.createElementNS(svgns, 'circle');
      circle.setAttribute('cx', x.toString());
      circle.setAttribute('cy', y.toString());
      circle.setAttribute('r', viewsize / 400);
      circle.setAttribute('fill', color);
      mapview.appendChild(circle);
    };

    // distribution plots:
    for (var u = 0; u < 1.0; u += 0.001) {
      plot(u * viewsize, viewsize - angle_distribution(u) * viewsize, 'blue');
      plot(u * viewsize, viewsize - radius_distribution(u) * viewsize, 'green');
    };

    // The star distribution:
    for (var n = 0; n < 1000; n++) {
      var radius = radius_distribution(Math.random())
      var angle = 2 * Math.PI * angle_distribution(Math.random());
      var spinangle = angle + 2*radius;

      var x = halfsize + halfsize * radius * Math.cos(spinangle);
      var y = halfsize + halfsize * radius * Math.sin(spinangle);

      plot(x, y, 'white');
    }
  });
