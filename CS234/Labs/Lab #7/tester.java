public class tester {
    public  static void main (String[] args) {
        
        // Croase a Hospital.
        Hospital stHellen = new Hospital("St Hellen");
        
        // Create two soldiers
        Soldier rambo = new Soldier();
        rambo.setHealth(5);
        rambo.setSoldierType("Green Beret");
        rambo.addWeapon("Bow & Arrow");
        rambo.addWeapon("Big knife");
        rambo.addWeapon("Bazzoka");
       
        Soldier bad_guy = new Soldier (5, "Sniper");
        bad_guy.addWeapon("Rifle");
        bad_guy.addWeapon("Pistol");
       
        System.out.println(rambo.getInfo());
        System.out.println(bad_guy.getInfo());

        rambo.shootEnemy(bad_guy);
        System.out.println(bad_guy.getInfo());
        rambo.shootEnemy(bad_guy);
        rambo.shootEnemy(bad_guy);
        rambo.shootEnemy(bad_guy);
        System.out.println(bad_guy.getInfo());
        stHellen.healPatient(bad_guy);
        System.out.println(bad_guy.getInfo());
        rambo.shootEnemy(bad_guy);
        rambo.shootEnemy(bad_guy);
        stHellen.healPatient(bad_guy);
        }
    }