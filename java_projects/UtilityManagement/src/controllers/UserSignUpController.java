package controllers;

import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Labeled;
import javafx.scene.control.TextField;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.sql.SQLException;

import dao.DBConnect;
import javafx.event.ActionEvent;

import javafx.scene.control.PasswordField;

public class UserSignUpController {
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

    private UserLoginController uL = new UserLoginController();
    private Labeled lblErrorMessage;
    
    DBConnect dbConnect = new DBConnect();

    // Set the reference to the UserLogin stage
    public static void setUserLoginStage(Stage stage) {
    }

    // Event Listener on Button[#btnBack].onAction
    @FXML
    public void handleBackButton(ActionEvent event) {
        Object userLoginStage = null;
        if (userLoginStage != null) {
            // If UserLogin stage is not null, bring it to the front
            ((Node) userLoginStage).toFront();
        } else {
            // If UserLogin stage is null, open a new instance
            openUserLoginPage(event);
        }

        // Close the current UserSignUp stage
        Stage userSignUpStage = (Stage) btnBack.getScene().getWindow();
        userSignUpStage.close();
    }

    private void openUserLoginPage(ActionEvent event) {
       

    }

    // Event Listener on Button[#btnClear].onAction
    @FXML
    public void handleClearButton(ActionEvent event) {
        // Clear all text fields and remove highlighting
        clearFields();
        // Clear error message
        lblErrorMessage.setText("");
    }
    
    // Event Listener on Button[#btnModify].onAction
    @FXML
    public void handleRegisterButton(ActionEvent event) {
       
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
            dbConnect.userSignUp(username, password, name, email, age, city, state, zipcode);
            showSuccessAlert("User signed up successfully!");
            	        
            } catch (SQLException e) {
            e.printStackTrace();
            // Handle the exception or provide feedback to the user about the failure
            System.out.println("Error during User sign-up: " + e.getMessage());
        }
    	// Check if any of the required fields are empty
		/*
		 * boolean hasEmptyFields = false;
		 * 
		 * if (txtName.getText().isEmpty()) { highlightField(txtName); hasEmptyFields =
		 * true; }
		 * 
		 * if (txtEmail.getText().isEmpty()) { highlightField(txtEmail); hasEmptyFields
		 * = true; }
		 * 
		 * if (txtUsername.getText().isEmpty()) { highlightField(txtUsername);
		 * hasEmptyFields = true; }
		 * 
		 * if (txtPassword.getText().isEmpty()) { highlightField(txtPassword);
		 * hasEmptyFields = true; }
		 * 
		 * if (txtAge.getText().isEmpty()) { highlightField(txtAge); hasEmptyFields =
		 * true; }
		 * 
		 * if (txtCity.getText().isEmpty()) { highlightField(txtCity); hasEmptyFields =
		 * true; }
		 * 
		 * if (txtState.getText().isEmpty()) { highlightField(txtState); hasEmptyFields
		 * = true; }
		 * 
		 * if (txtZipcode.getText().isEmpty()) { highlightField(txtZipcode);
		 * hasEmptyFields = true; }
		 * 
		 * // If any required field is empty, display a message if (hasEmptyFields) {
		 * lblErrorMessage.setText("Please fill in all required fields."); } else { //
		 * Clear highlighting when all fields are filled clearFields(); // Clear error
		 * message lblErrorMessage.setText("");
		 * 
		 * }
		 */
    }
    
    private void highlightField(TextField textField) {
        // Set red border around the empty field
        textField.setStyle("-fx-border-color: red;");

        // Remove red border when the field is filled
        textField.textProperty().addListener((observable, oldValue, newValue) -> {
            if (!newValue.isEmpty()) {
                textField.setStyle("");
            }
        });
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
        txtZipcode.setStyle("");}
        
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
    


