
function copyData() {
  // IDs of the source and target spreadsheets
  var sourceSpreadsheetId = '106-geoIDoX82CEk';
  var targetSpreadsheetId = '1XqaTbzgm6WSGbBfn6Xc';

  // sheet name
  var source_sheet = 'AmazonDisplay_CampaignAudit'
  var target_sheet = 'Meta Campaign Test'
  
  // Get the source and target spreadsheets
  var sourceSpreadsheet = SpreadsheetApp.openById(sourceSpreadsheetId);
  var targetSpreadsheet = SpreadsheetApp.openById(targetSpreadsheetId);
  
  // Get the source and target sheets by name
  var sourceSheet = sourceSpreadsheet.getSheetByName(source_sheet);
  var targetSheet = targetSpreadsheet.getSheetByName(target_sheet);
  
  // Get the data range from the source sheet
  var sourceRange = sourceSheet.getDataRange();
  var data = sourceRange.getValues();
  
  // Clear the target sheet (optional)
  targetSheet.clear();
  
  // Set the values in the target sheet
  targetSheet.getRange(1, 1, data.length, data[0].length).setValues(data);
}

