(function($) {
    $(function() {

        $('.button-collapse').sideNav();
        $('.parallax').parallax(

        );
        $('.modal').modal();
        $('.carousel').carousel({
            dist: 0
        });
        $('ul.tabs').tabs({

        });
        $('select').material_select();
         $('.dropdown-button').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrainWidth: true, // Does not change width of dropdown to that of the activator
      hover: true, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: false, // Displays dropdown below the button
      alignment: 'left', // Displays dropdown with edge aligned to the left of button
      stopPropagation: false // Stops event propagation
    }
  );

    }); // end of document ready
})(jQuery); // end of jQuery name space


$(document).ready(function () {
    $('#showSteps').click(function () {
            $('.menuSteps').show('slow');
            $("#wheretogo").hide('fast');

    });
    $('#opensearch').click( function () {
        $('#searchform').show('slow');
    })
})
