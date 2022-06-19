package fcsc;

import java.util.Scanner;

public class Mdp {
	public static void main(String[] arrstring) {
		final String s = "4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_";
		System.out.print("Mot de passe est :" + show(s));
		final Scanner scanner = new Scanner(System.in);
		System.out.print("Mot de passe Admin:");
		final String string2 = scanner.nextLine();
		if (s.equals(Mdp.hide(string2))) {
			System.out.println("Bienvenue Admin");
		} else {
			System.out.println("Au revoir non admin");
		}
	}

	static String hide(String string) {
		String s = "";
		for (int i = 0; i < string.length(); ++i) {
			char c = string.charAt(i);
			c = (char) (c - i);
			c = (char) (c % 128);
			s = s + c;
		}
		return s;
	}

	static String show(String source) {
		String s = "";
		for (int i = 0; i < source.length(); ++i) {
			char c = source.charAt(i);
			c = (char) (c + i);
			c = (char) (c % 128);
			s = s + c;
		}
		return s;
	}
}
