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

public class UserLoginController {
	DBConnect dbConnect = new DBConnect(); 
    @FXML
    private TextField txtUserId;

    @FXML
    private PasswordField txtUserPassword;

    @FXML
    private Button btnUserLogin;

    @FXML
    private Button btnBack;

    @FXML
    private Button btnSignUp;

    private static Stage homeStage;

    @FXML
    public void userLogin(ActionEvent event) {
        // Open UserHomeController when the login button is pressed
    	// Fetch the entered admin ID and password
        String enteredUsername = txtUserId.getText();
        String enteredPassword = txtUserPassword.getText();

        // Implement admin login logic here
        if (dbConnect.authenticateUser(enteredUsername, enteredPassword)) {
            // Assuming login is successful, open the AdminHomeController
        	Stage userLoginStage = (Stage) btnBack.getScene().getWindow();
            userLoginStage.close();
            //load admin homepage
            openUserHomeController();
        } else {
            // Display an error message for unsuccessful login
            showAlert("Login Error", "Invalid username or password.");
        }
    }

    private void openUserHomeController() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("UserHome.fxml"));
            Parent root = loader.load();

            // Access the controller of UserHome.fxml
            UserHomeController homeController = loader.getController();

            // Optionally pass any necessary data to the controller before showing the stage
            // homeController.setData(...);

            Scene scene = new Scene(root);

            // Use the class-level homeStage variable instead of creating a new one
            homeStage = new Stage();
            homeStage.setTitle("User Home");
            homeStage.setScene(scene);

            // Set the UserHomeController's SceneController reference
            homeController.setSceneController(new SceneController());

            homeStage.show();  // Show the stage after setting it up
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void backToHome(ActionEvent event) {
        if (homeStage == null) {
            // If homepage stage is not already open, create a new instance
            openHomePage(event);
        } else {
            // If homepage stage is already open, bring it to the front
            homeStage.toFront();
        }

        // Close the current user login stage
        Stage userLoginStage = (Stage) btnBack.getScene().getWindow();
        userLoginStage.close();
    }

    public void openHomePage(ActionEvent event) {
        // Close the current user login stage and open the HomePage
        Stage userStage = (Stage) btnBack.getScene().getWindow();
        userStage.close();

        try {
            Parent root = FXMLLoader.load(getClass().getResource("Scene.fxml"));
            Scene scene = new Scene(root);

            // Set the homeStage variable to null when going back to the home page
            homeStage = null;

            //Stage homeStage = new Stage();
            homeStage.setTitle("Home");
            homeStage.setScene(scene);
            homeStage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void signUp(ActionEvent event) {
        // Load the UserSignUp.fxml file and show the associated controller
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("UserSignUp.fxml"));
            Parent root = loader.load();

            // Get the controller associated with the loaded FXML
            UserSignUpController userSignUpController = loader.getController();

            // Set the reference to the user sign up stage
            userSignUpController.setUserLoginStage(homeStage);

            // Create a new stage for the UserSignUp scene
            Stage userSignUpStage = new Stage();
            userSignUpStage.setTitle("User Sign Up");
            userSignUpStage.setScene(new Scene(root));
            userSignUpStage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    private boolean authenticateUser(String username, String password) {
    	DBConnect dbConnect = new DBConnect(); 
    	
        // Query the database to check if the entered credentials are valid
        String query = "SELECT * FROM ums_user_login WHERE username = ? AND password = ?";
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
