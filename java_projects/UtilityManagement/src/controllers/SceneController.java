package controllers;


import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.fxml.Initializable;
import javafx.scene.control.TextField;
import javafx.scene.image.ImageView;
import javafx.event.EventHandler;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;
import java.util.ResourceBundle;
import javafx.scene.effect.DropShadow;

import java.net.URL;

import javafx.application.Platform;
import javafx.event.ActionEvent;

public class SceneController implements Initializable {
	@FXML
    private ImageView imgbtn_admin;
    @FXML
    private ImageView imgbtn_user;
    @FXML
    private ImageView imgbtn_logout;
	
	private static Stage adminStage;
	private static Stage userStage;

	
	@Override
    public void initialize(URL location, ResourceBundle resources) {
		
		// Add event handlers
		 imgbtn_admin.setOnMouseClicked(event -> handleAdminButton(event));
	        imgbtn_admin.setOnMouseEntered(event -> handleMouseEnter(event));
	        imgbtn_admin.setOnMouseExited(event -> handleMouseExit(event));

	        imgbtn_user.setOnMouseClicked(event -> handleUserButton(event));
	        imgbtn_user.setOnMouseEntered(event -> handleMouseEnter(event));
	        imgbtn_user.setOnMouseExited(event -> handleMouseExit(event));

	        imgbtn_logout.setOnMouseClicked(event -> handleLogoutButton(event));
	        imgbtn_logout.setOnMouseEntered(event -> handleMouseEnter(event));
	        imgbtn_logout.setOnMouseExited(event -> handleMouseExit(event));
	    }
	
		/*
		 * private Object handleMouseExit(MouseEvent event) { // TODO Auto-generated
		 * method stub return null; }
		 * 
		 * private Object handleMouseEnter(MouseEvent event) { // TODO Auto-generated
		 * method stub return null; }
		 */
	
	   private void handleMouseEnter(MouseEvent event) {
	        ImageView source = (ImageView) event.getSource();
	        DropShadow dropShadow = new DropShadow();
	        source.setEffect(dropShadow);
	    }

	    private void handleMouseExit(MouseEvent event) {
	        ImageView source = (ImageView) event.getSource();
	        source.setEffect(null);
	    }
	

	private void handleAdminButton(MouseEvent mouseEvent) {
        if (adminStage == null) {
            // If Admin login stage is not already open, create a new instance
            openAdminLoginPage(mouseEvent);
        } else {
        	
            // If Admin login stage is already open, bring it to the front
            adminStage.toFront();
        }
    }
	// code for logout button to exit application
	private void handleLogoutButton(MouseEvent event) {
        Stage stage = (Stage) imgbtn_logout.getScene().getWindow();
        stage.close(); // Close the current stage (application window)
        Platform.exit();
    }

	private void openAdminLoginPage(MouseEvent mouseEvent) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("AdminLogin.fxml"));
            Scene scene = new Scene(root);
            
            Stage adminStage = new Stage();
            adminStage.setTitle("Admin Login");
            adminStage.setScene(scene);
            adminStage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
	
	 private void handleUserButton(MouseEvent mouseEvent) {
		 if (userStage == null) {
	            // If Admin login stage is not already open, create a new instance
			 openUserLoginPage(mouseEvent);
	        } else {
	            // If Admin login stage is already open, bring it to the front
	            userStage.toFront();
	        }
	    }
	 
	 private void openUserLoginPage(MouseEvent mouseEvent) {
	        try {
	            Parent root = FXMLLoader.load(getClass().getResource("UserLogin.fxml"));
	            Scene scene = new Scene(root);
	            
	            Stage userStage = new Stage();
	            userStage.setTitle("User Login");
	            userStage.setScene(scene);
	            userStage.show();
	        } catch (Exception e) {
	            e.printStackTrace();
	        }
	    }

	public void setUserStage(Stage homeStage) {
		// TODO Auto-generated method stub
		
	}
	
}
