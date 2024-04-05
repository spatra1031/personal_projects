package controllers;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import dao.DBConnect;


public class AdminLogin {
	DBConnect dbConnect = new DBConnect(); 
	@FXML
    private Label lblAdminId; 
    @FXML
    private Label lblAdminPassword; 
    @FXML
    private TextField txtAdminId;
    @FXML
    private PasswordField txtAdminPassword;
    @FXML
    private Button btnAdminLogin;
    @FXML
    private Button btnBack;
    private static Stage homeStage;
  

    @FXML
    public void adminLogin(ActionEvent event) {
    	// Fetch the entered admin ID and password
        String enteredUsername = txtAdminId.getText();
        String enteredPassword = txtAdminPassword.getText();

        // Implement admin login logic here
        if (dbConnect.authenticateAdmin(enteredUsername, enteredPassword)) {
            // Assuming login is successful, open the AdminHomeController
        	Stage adminLoginStage = (Stage) btnBack.getScene().getWindow();
            adminLoginStage.close();
            //load admin homepage
            openAdminHomeController();
        } else {
            // Display an error message for unsuccessful login
            showAlert("Login Error", "Invalid username or password.");
        }
    }

    private void openAdminHomeController() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("AdminHome.fxml"));
            Parent root = loader.load();

            // Access the controller of AdminHome.fxml
            AdminHomeController homeController = loader.getController();

            // Optionally pass any necessary data to the controller before showing the stage
            // homeController.setData(...);

            Scene scene = new Scene(root);

            // Use the class-level homeStage variable instead of creating a new one
            homeStage = new Stage();
            homeStage.setTitle("Admin Home");
            homeStage.setScene(scene);

            // Set the AdminHomeController's SceneController reference
            homeController.setSceneController(new SceneController());

            homeStage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
 // Event Listener on Button[#btnBack].onAction
    @FXML
    public void backToHome(ActionEvent event) {
        if (homeStage == null) {
            // If homepage stage is not already open, create a new instance
            openHomePage( event);
        } else {
            // If homepage stage is already open, bring it to the front
            homeStage.toFront();
        }

        // Close the current admin login stage
        Stage adminLoginStage = (Stage) btnBack.getScene().getWindow();
        adminLoginStage.close();
    }
    public void openHomePage(ActionEvent event) {
        // Close the current admin login stage and open the HomePage
        Stage adminStage = (Stage) btnBack.getScene().getWindow();
        adminStage.close();

        try {
            Parent root = FXMLLoader.load(getClass().getResource("Scene.fxml"));
            Scene scene = new Scene(root);
            
            
           //Stage homeStage = new Stage();
            homeStage.setTitle("Home");
            homeStage.setScene(scene);
            homeStage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

	/*
	 * private void handleBackButton(ActionEvent event) { if (homeStage == null) {
	 * // If homepage stage is not already open, create a new instance
	 * openHomePage(event); } else { // If homepage stage is already open, bring it
	 * to the front homeStage.toFront(); } }
	 */
    @FXML
    public void signUp(ActionEvent event) {
        // Open the AdminSignUp.fxml file when the "Sign Up" button is clicked
        openAdminSignUpPage();
        Stage adminLoginStage = (Stage) btnBack.getScene().getWindow();
        adminLoginStage.close();
        
    }

    private void openAdminSignUpPage() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("AdminSignUp.fxml"));
            Parent root = loader.load();

            // Access the controller of AdminSignUp.fxml
            AdminSignUpController signUpController = loader.getController();

            // Optionally pass any necessary data to the controller before showing the stage
            // signUpController.setData(...);

            Scene scene = new Scene(root);

            // Use the class-level homeStage variable instead of creating a new one
            homeStage = new Stage();
            homeStage.setTitle("Admin Sign Up");
            homeStage.setScene(scene);
            homeStage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    private boolean authenticateAdmin(String username, String password) {
    	DBConnect dbConnect = new DBConnect(); 
    	
        // Query the database to check if the entered credentials are valid
        String query = "SELECT * FROM ums_admin_login WHERE username = ? AND password = ?";
        try (PreparedStatement statement = dbConnect.getConnection().prepareStatement(query)) {
            statement.setString(1, username);
            statement.setString(2, password);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next(); // Returns true if there is a matching record
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    private void showAlert(String title, String content) {
        // Display an alert with the specified title and content
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle(title);
        alert.setContentText(content);
        alert.showAndWait();
    }
}
