import java.util.ArrayList;

public class Display
{
    public static void displayTest(ArrayList<ArrayList<ArrayList<Object>>> _plate)
    {
        for(int i = 0; i < _plate.size(); i++)
        {
            for(int j = 0; j < _plate.get(0).size(); j++)
            {
                System.out.println(_plate.get(i).get(j).get(0) + "\t");
            }
            System.out.println();
        }
    }

    public static String emoji(Object _obj)
    {
        String m = "";
        if (_obj.getDesc() == "baba")
            m = "😀";
        else if (_obj.getDesc() == "flag")
            m = "🏁";
        else if (_obj.getDesc() == "wall")
            m = "🧱";
        else if (_obj.getDesc() == "rock")
            m = "🪨 ";
        else if (_obj.getDesc() == "metal") 
            m = "0️ ";
        else if (_obj.getDesc() == "goop")
            m = "🌊";
        else if (_obj.getDesc() == "grass")
            m = "🌿";
        else if (_obj.getDesc() == "lava")
            m = "🌋";
        else if (_obj.getDesc() == "text_baba")
            m = "🇧 ";
        else if (_obj.getDesc() == "text_flag")
            m = "🇫 ";
        else if (_obj.getDesc() == "text_wall")
            m = "🇼 ";
        else if (_obj.getDesc() == "text_rock")
            m = "🇷 ";
        else if (_obj.getDesc() == "text_grass")
            m = "🇬 ";
        else if (_obj.getDesc() == "text_goop")
            m = "🇴 ";
        else if (_obj.getDesc() == "text_lava")
            m = "🇱 ";
        else if (_obj.getDesc() == "is")
            m = "✔️ ";
        else if (_obj.getDesc() == "stop")
            m = "⛔";
        else if (_obj.getDesc() == "push")
            m = "💪";
        else if (_obj.getDesc() == "you")
            m = "👇";
        else if (_obj.getDesc() == "win")
            m = "🎆";
        else if (_obj.getDesc() == "best")
            m = "✨";
        else if (_obj.getDesc() == "sink")
            m = "🚰";
        else if (_obj.getDesc() == "kill")
            m = "☠️ ";
        
        return m;
    }

    public static void menu()
    {

    }

    public static void edit()
    {

    }

    public static void play()
    {

    }

    public static void animation()
    {
        
    }
}