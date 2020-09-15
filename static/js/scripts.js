'use strict';

/**
 * Sanity.UI: Dialog
 * Version: 1.2.5 (14/04/2020)
 */
class _sanityUiDialog {
    constructor(dialog, options) {
        this.mOptions = {
            timeout: 1,
            trigger: null,
            canClose: true,
            hrefNavigation: true,
        };
        this.mElements = {
            dialog: null,
            content: null,
            close: null,
        };
        this.mWorking = false;
        $.extend(this.mOptions, options);
        this.mElements.dialog = dialog;
        this.mElements.dialog.addClass('sanity_ui_dialog');
        // If content in not wrapped, wrap it
        if (!$('> .sanity_ui_dialog__content', this.mElements.dialog).length) {
            dialog.wrapInner('<div class="sanity_ui_dialog__content">');
        }
        this.mElements.content = $('> .sanity_ui_dialog__content', dialog);
        // If close button exist - bind it, else create it
        if (this.mOptions.canClose) {
            if ($('> .sanity_ui_dialog__close', this.mElements.content).length) {
                this.mElements.close = $('> .sanity_ui_dialog__close', this.mElements.content);
            } else {
                this.mElements.close = $('<button class="btn btn_close sanity_ui_dialog__close"></button>').appendTo(this.mElements.content);
            }
        }
        // If trigger is not set from JS, set it from HTML (html is prefered method)
        if (!this.mOptions.trigger) {
            this.mOptions.trigger = this.mElements.dialog.attr('data-sanity_ui_dialog');
        }
        // If link contains hash with dialog trigger - open it
        if (this.mOptions.hrefNavigation) {
            if (window.location.hash === '#dialog_' + this.mOptions.trigger) {
                this.showDialog();
            }
        }
        // Open dialog on trigger click
        $('[data-sanity_ui_dialog_trigger="' + this.mOptions.trigger + '"]').on('click', () => {
            this.openDialog();
        });
        // Open event for dialog
        $(this.mElements.dialog).on('sanity.ui.dialog.open', (event, params) => {
            this.openDialog();
        });
        // Hide dialog if clicked something not close button or overlay
        if (this.mOptions.canClose) {
            $(this.mElements.dialog).on('click', (e) => {
                let target = $(e.target);
                if (target.is(this.mElements.dialog) || target.is(this.mElements.close) || target.is($('*', this.mElements.close))) {
                    this.closeDialog();
                }
            });
        }
        // Close event for dialog
        $(this.mElements.dialog).on('sanity.ui.dialog.close', (event, params) => {
            this.closeDialog();
        });

        $(this.mElements.dialog).on('sanity.ui.dialog.show', (event, params) => {
            this.showDialog();
        });

        $(this.mElements.dialog).on('sanity.ui.dialog.hide', (event, params) => {
            this.hideDialog();
        });

        if (this.mOptions.hrefNavigation) {
            // Binding popstate event
            $(window).bind('popstate', (e) => {
                // If popstate to something - hide dialog, else show it
                if (window.location.hash !== '#dialog_' + this.mOptions.trigger) {
                    if (this.mOptions.canClose) {
                        this.hideDialog();
                    }
                } else {
                    this.showDialog();
                }
            });
        }
    }

    openDialog() {
        if (window.location.hash !== '#dialog_' + this.mOptions.trigger && this.mOptions.hrefNavigation) {
            window.location.hash = '#dialog_' + this.mOptions.trigger;
        } else {
            this.showDialog();
        }
    }

    closeDialog() {
        if (this.mOptions.canClose) {
            if (window.location.hash === '#dialog_' + this.mOptions.trigger && this.mOptions.hrefNavigation) {
                if (history.length > 1) {
                    history.back();
                } else {
                    _sanityUiUtils.removeLocationHash();
                    this.hideDialog();
                }
            } else {
                this.hideDialog();
            }
        }
    }

    showDialog() {
        if (!this.mWorking && !this.mElements.dialog.hasClass('sanity_ui_dialog_display')) {
            this.mWorking = true;
            this.mElements.dialog.addClass('sanity_ui_dialog_display');
            $('html').addClass('overflow_hidden--sanity_ui_dialog');
            this.mElements.dialog.removeClass('sanity_ui_dialog_out').addClass('sanity_ui_dialog_in');
            this.mElements.dialog.one('webkitAnimationEnd oanimationend msAnimationEnd animationend', () => {
                this.mWorking = false;
                this.mElements.dialog.trigger('sanity.ui.dialog.shown');
            });
        }
    };

    hideDialog() {
        if (!this.mWorking && this.mElements.dialog.hasClass('sanity_ui_dialog_display')) {
            this.mWorking = true;
            this.mElements.dialog.removeClass('sanity_ui_dialog_in').addClass('sanity_ui_dialog_out');
            this.mElements.dialog.one('webkitAnimationEnd oanimationend msAnimationEnd animationend', () => {
                this.mWorking = false;
                this.mElements.dialog.removeClass('sanity_ui_dialog_display');
                if (window.location.hash.includes('#dialog_')) {
                    // Do not hide overflow, because we still have dialog window
                } else {
                    $('html').removeClass('overflow_hidden--sanity_ui_dialog');
                }
                this.mElements.dialog.trigger('sanity.ui.dialog.hidden');
            });
        }
    };
}

$(function () {
    let mOutput, mInput, mLock = null;

    function lock() {
        mLock = $('<div class="col flex_center flex_align-items_center lock"><div class="loader"></div></div>').appendTo('body');
    }

    function unlock() {
        if (mLock)
            mLock.remove();
    }

    function disable() {
        $('.submit, .section__item__control .btn').addClass('btn_disabled');
        $('.input_text__input').attr('disabled', true);
    }

    function enable() {
        $('.submit, .section__item__control .btn').removeClass('btn_disabled');
        $('.input_text__input').attr('disabled', false);
    }

    function setOutput(text) {
        mOutput.html('<p>' + text + '</p>');
    }

    function submit(type, content) {
        let timeout = 1000;
        $.ajax({
            url: 'http://127.0.0.1:5000/run',
            type: 'POST',
            data: {
                type: type,
                text: content
            },
            beforeSend: () => {
                disable();
                lock();
            },
            success: (response) => {
                console.log(response);
                setTimeout(() => {
                    enable();
                    unlock();
                    if ('status' in response && response.status === 'ok' && 'data' in response && response.data) {
                        setOutput(response.data);
                    } else {
                        if ('message' in response) {
                            setOutput(response.message);
                        } else {
                            setOutput('Unknown error');
                        }
                    }
                }, timeout);
            },
            error: (response) => {
                console.log(response);
                setTimeout(() => {
                    enable();
                    unlock();
                    setOutput('Unknown error');
                }, timeout);
            },
            complete: (response) => {

            },
        });
    }

    function copy() {
        $('#output').select();
        document.execCommand('copy');
    }

    function download(filename, text) {
        let element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', filename);
        element.style.display = 'none';
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    }

    $(document).ready(function () {
        mInput = $('#input');
        mOutput = $('#output');
        // Сабмит
        let submitButton = $('.submit');
        submitButton.on('click', function () {
            let type = $(this).attr('data-type');
            if (!type)
                type = 'default'
            submit(type, mInput.val());
        });
        // Копировать
        let copyButton = $('.copy');
        copyButton.hover(function () {
            $(this).attr('data-sanity_ui_tooltip', 'Копировать');
        });
        copyButton.on('click', function () {
            $(this).attr('data-sanity_ui_tooltip', 'Скопировано');
            copy();
        });
        // Печать
        let printButton = $('.print');
        printButton.on('click', function () {

        });
        // Скачать
        let downloadButton = $('.download');
        downloadButton.on('click', function () {
            download('output.txt', mOutput.text());
        });
        // Справка
        new _sanityUiDialog($('[data-sanity_ui_dialog="help"]'));
    });
});