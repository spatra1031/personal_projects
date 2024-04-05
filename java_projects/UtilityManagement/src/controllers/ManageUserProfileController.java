package controllers;

import java.sql.SQLException;

import dao.DBConnect;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Labeled;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class ManageUserProfileController {

    @FXML
    private TextField txtName;

    @FXML
    private TextField txtEmail;

    @FXML
    private TextField txtUsername;

    @FXML
    private PasswordField txtPassword;

    @FXML
    private TextField txtAge;

    @FXML
    private TextField txtCity;

    @FXML
    private TextField txtState;

    @FXML
    private TextField txtZipcode;

    @FXML
    private Button btnBack;

    @FXML
    private Button btnClear;

    @FXML
    private Button btnModify;

    private Stage userProfileStage; // Reference to the stage

    private Labeled lblErrorMessage;
	DBConnect dbConnect = new DBConnect();
    
	/*
	 * public void setUserProfileStage(Stage userProfileStage) {
	 * this.userProfileStage = userProfileStage; }
	 */

    @FXML
    void handleBackButton(ActionEvent event) {
        // TODO: Implement back button logic
        userProfileStage.close(); // Close the current stage
    }

    @FXML
    public void handleClearButton(ActionEvent event) {
        // Clear all text fields and remove highlighting
        clearFields();
        // Clear error message
        lblErrorMessage.setText("");
        
    }
        
        private void clearFields() {
	        // Clear all text fields and remove highlighting
	        txtName.clear();
	        txtEmail.clear();
	        txtUsername.clear();
	        txtPassword.clear();
	        txtAge.clear();
	        txtCity.clear();
	        txtState.clear();
	        txtZipcode.clear();

	        // Reset styles (remove red border)
	        txtName.setStyle("");
	        txtEmail.setStyle("");
	        txtUsername.setStyle("");
	        txtPassword.setStyle("");
	        txtAge.setStyle("");
	        txtCity.setStyle("");
	        txtState.setStyle("");
	        txtZipcode.setStyle("");
	    }
        
        @FXML
	    public void handleModifyButton(ActionEvent event) {
	       
	        // Capture data from input fields
	        String name = txtName.getText();
	        String email = txtEmail.getText();
	        String username = txtUsername.getText();
	        String password = txtPassword.getText();
	        // Parse age to an int (you might want additional validation here)
	        int age = Integer.parseInt(txtAge.getText());
	        String city = txtCity.getText();
	        String state = txtState.getText();
	        int zipcode = Integer.parseInt(txtZipcode.getText());

	        try {
	            // Call adminSignUp method from DBConnect
	            dbConnect.userModify(username, password, name, email, age, city, state, zipcode);
	            showSuccessAlert("Data Modified successfully!");
	            	        
	            } catch (SQLException e) {
	            e.printStackTrace();
	            // Handle the exception or provide feedback to the user about the failure
	            System.out.println("Error during modification: " + e.getMessage());
	        }
        }

        // Helper method to show a success alert
	    private void showSuccessAlert(String message) {
	        Alert alert = new Alert(Alert.AlertType.INFORMATION);
	        alert.setTitle("Success");
	        alert.setHeaderText(null);
	        alert.setContentText(message);
	        alert.showAndWait();
	    }
	    private void showAlert(String title, String content) {
	        Alert alert = new Alert(Alert.AlertType.INFORMATION);
	        alert.setTitle(title);
	        alert.setContentText(content);
	        alert.showAndWait();
	    }
}
