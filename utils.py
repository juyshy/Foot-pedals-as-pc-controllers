
import win32clipboard as wc
import win32con
import platform
import Tkinter as tk
root = tk.Tk()
root.withdraw()


from subprocess import Popen, PIPE

platform_info=platform.platform()

if "Windows" in platform_info:
    def copy_to_clipboard(msg):
        """ Copy to clipboard

        :param msg:
        :return:
        """
        if sys.platform == 'win32':
            wc.OpenClipboard()  # pylint: disable=no-member
            wc.EmptyClipboard()  # pylint: disable=no-member
            wc.SetClipboardData(win32con.CF_TEXT, msg)  # pylint: disable=no-member
            wc.CloseClipboard()  # pylint: disable=no-member


    def paste_from_clipboard():
        """ Paste from clipboard

        :return:
        """
        wc.OpenClipboard()  # pylint: disable=no-member
        msg = wc.GetClipboardData(win32con.CF_TEXT)  # pylint: disable=no-member
        wc.CloseClipboard()  # pylint: disable=no-member
        return msg

else:
    p = Popen(['xsel', '-pi'], stdin=PIPE)
    p.communicate(input='Hello, World')
    def copy_to_clipboard(str, p=True, c=True):
        from subprocess import Popen, PIPE

        if p:
            p = Popen(['xsel', '-pi'], stdin=PIPE)
            p.communicate(input=str)
        if c:
            p = Popen(['xsel', '-bi'], stdin=PIPE)
            p.communicate(input=str)


    def paste_from_clipboard():
        """ Paste from clipboard

        :return:
        """
        c = root.clipboard_get()
        return c

