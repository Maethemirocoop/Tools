import cv2
# Fonction de rappel pour capturer les clics de souris
def afficher_coordonnees(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:  # Si le bouton gauche de la souris est cliqué
        print(f"Coordonnées : X={x}, Y={y}")
        # Affiche les coordonnées sur l'image
        cv2.putText(img, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        cv2.imshow("Image", img)

# Charger une image

chemin_image = r"C:\Users\maeva_hkbgytx\OneDrive\Images\JPM_PR_visual_mid.png" # Remplacez par le chemin de votre image
img = cv2.imread(chemin_image)

if img is None:
    print("Erreur : Impossible de charger l'image. Vérifiez le chemin.")
else:
    # Afficher l'image dans une fenêtre
    cv2.imshow("Image", img)
    # Associer la fonction de rappel à la fenêtre
    cv2.setMouseCallback("Image", afficher_coordonnees)
    # Attendre que l'utilisateur appuie sur une touche pour fermer
    cv2.waitKey(0)
    cv2.destroyAllWindows()