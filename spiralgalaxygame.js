window.addEventListener(
  'load',
  function () {
    var svgns = 'http://www.w3.org/2000/svg';
    var mapview = document.getElementById('mapview');
    var viewsize = 1000;
    var halfsize = viewsize / 2;
    var starradius = {
      min: viewsize / 4000,
      max: viewsize / 800,
      };
    starradius.range = starradius.max - starradius.min;

    var param = {
      tightness: 0.35,
      spokes: 4,
      spin: 3.8,
      diffusion: 13.5,
    };

    var radius_distribution = function (u) {
      var a = Math.pow(Math.sin(0.5 * Math.PI * u), param.tightness);
      var b = u * u;

      return (a + b*b) / 2;
    };

    var angle_distribution = function (u) {
      var factor = param.spokes * Math.PI;
      var a = Math.sin(factor * u);
      var b = Math.pow(Math.abs(a), param.diffusion);
      return u - b / factor;
    };

    var star_radius_distribution = function (u) {
      return starradius.min + starradius.range * Math.pow(u, 2);
    };

    var plot = function (x, y, radius, color) {
      var circle = document.createElementNS(svgns, 'circle');
      circle.setAttribute('cx', x.toString());
      circle.setAttribute('cy', y.toString());
      circle.setAttribute('r', radius);
      circle.setAttribute('fill', color);
      mapview.appendChild(circle);
    };

    // distribution plots:
    /*
    for (var u = 0; u < 1.0; u += 0.001) {
      var x = u * viewsize;
      var y_of = function (yu) { return viewsize - yu * viewsize };

      plot(x, y_of(angle_distribution(u)), starradius.max, 'blue');
      plot(x, y_of(radius_distribution(u)), starradius.max, 'green');
    };
    */

    // The star distribution:
    for (var n = 0; n < 3000; n++) {
      var radius = radius_distribution(Math.random())
      var angle = 2 * Math.PI * angle_distribution(Math.random());
      var srad = star_radius_distribution(Math.random());
      var spinangle = angle + param.spin * radius;

      var x = halfsize + halfsize * radius * Math.cos(spinangle);
      var y = halfsize + halfsize * radius * Math.sin(spinangle);

      plot(x, y, srad, 'white');
    }
  });
