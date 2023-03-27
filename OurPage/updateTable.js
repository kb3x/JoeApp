
function updateTable() {
    // Make an AJAX request to your Flask server to retrieve the latest data from your database
    $.ajax({
      url: '/',
      type: 'GET',
      success: function(rows_html) {
        // Replace the existing rows in the table with the new rows
        $('#myTable tbody').html(rows_html);
      }
    });
  }
  
  // Call the updateTable function every 5 seconds
  setInterval(updateTable, 5000);