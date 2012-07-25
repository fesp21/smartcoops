<h1> Sign up</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="/polls/{{ poll.id }}/vote/" method="post">
{% csrf_token %}
{% for choice in poll.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>

<h1>Sign up</h1>
<div id="content-main">
<form enctype="multipart/form-data" action="" method="post" id="farmer_form"><div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='4QKdkVzXQZULYw1ubkPRA7GxmCSeAWLV' /></div>
<div>
<fieldset class="module aligned ">
<div class="form-row field-name">
<div>
<label for="id_name" class="required">Name:</label>
<input id="id_name" type="text" class="vTextField" name="name" maxlength="200" />
</div>
</div>
<div class="form-row field-coop">
<div>
<label for="id_coop" class="required">Coop:</label>
<select name="coop" id="id_coop">
<option value="" selected="selected">---------</option>
<option value="1">San Benito</option>
<option value="2">Seed Growers Cooperative of Laguna</option>
</select><a href="/admin/bookkeeper/coop/add/" class="add-another" id="add_id_coop" onclick="return showAddAnotherPopup(this);"> <img src="/static/admin/img/icon_addlink.gif" width="10" height="10" alt="Add Another"/></a>
</div>
</div>
</fieldset>
<fieldset class="module aligned ">
<h2>Contact information</h2>
<div class="form-row field-contactTelNum">
<div>
<label for="id_contactTelNum" class="required">Telephone:</label>
<input id="id_contactTelNum" type="text" class="vTextField" name="contactTelNum" maxlength="200" />
</div>
</div>
<div class="form-row field-contactMobileNum">
<div>
<label for="id_contactMobileNum" class="required">Mobile:</label>
<input id="id_contactMobileNum" type="text" class="vTextField" name="contactMobileNum" maxlength="200" />
</div>
</div>
<div class="form-row field-contactEmail">
<div>
<label for="id_contactEmail" class="required">Email:</label>
<input id="id_contactEmail" type="text" class="vTextField" name="contactEmail" maxlength="75" />
</div>
</div>
</fieldset>
<fieldset class="module aligned ">
<h2>Financial</h2>
<div class="form-row field-loanBalance">
<div>
<label for="id_loanBalance" class="required">LoanBalance:</label>
<input type="text" name="loanBalance" id="id_loanBalance" />
</div>
</div>
<div class="form-row field-savingsBalance">
<div>
<label for="id_savingsBalance" class="required">SavingsBalance:</label>
<input type="text" name="savingsBalance" id="id_savingsBalance" />
</div>
</div>
</fieldset>
<div class="inline-group" id="cultivation_set-group">
<div class="tabular inline-related last-related">
<input type="hidden" name="cultivation_set-TOTAL_FORMS" value="3" id="id_cultivation_set-TOTAL_FORMS" /><input type="hidden" name="cultivation_set-INITIAL_FORMS" value="0" id="id_cultivation_set-INITIAL_FORMS" /><input type="hidden" name="cultivation_set-MAX_NUM_FORMS" id="id_cultivation_set-MAX_NUM_FORMS" />
<fieldset class="module">
<h2>Cultivations</h2>
<table>
<thead><tr>
<th colspan="2" class="required">Crop
</th>
<th class="required">Hectare
</th>
<th>Delete?</th>
</tr></thead>
<tbody>
<tr class="form-row row1 "
id="cultivation_set-0">
<td class="original">
<input type="hidden" name="cultivation_set-0-id" id="id_cultivation_set-0-id" />
<input type="hidden" name="cultivation_set-0-farmer" id="id_cultivation_set-0-farmer" />
</td>
<td class="field-crop">
<select name="cultivation_set-0-crop" id="id_cultivation_set-0-crop">
<option value="" selected="selected">---------</option>
<option value="2">Rice</option>
</select><a href="/admin/bookkeeper/crop/add/" class="add-another" id="add_id_cultivation_set-0-crop" onclick="return showAddAnotherPopup(this);"> <img src="/static/admin/img/icon_addlink.gif" width="10" height="10" alt="Add Another"/></a>
</td>
<td class="field-hectare">
<input type="text" name="cultivation_set-0-hectare" id="id_cultivation_set-0-hectare" />
</td>
<td class="delete"></td>
</tr>
<tr class="form-row row2 "
id="cultivation_set-1">
<td class="original">
<input type="hidden" name="cultivation_set-1-id" id="id_cultivation_set-1-id" />
<input type="hidden" name="cultivation_set-1-farmer" id="id_cultivation_set-1-farmer" />
</td>
<td class="field-crop">
<select name="cultivation_set-1-crop" id="id_cultivation_set-1-crop">
<option value="" selected="selected">---------</option>
<option value="2">Rice</option>
</select><a href="/admin/bookkeeper/crop/add/" class="add-another" id="add_id_cultivation_set-1-crop" onclick="return showAddAnotherPopup(this);"> <img src="/static/admin/img/icon_addlink.gif" width="10" height="10" alt="Add Another"/></a>
</td>
<td class="field-hectare">
<input type="text" name="cultivation_set-1-hectare" id="id_cultivation_set-1-hectare" />
</td>
<td class="delete"></td>
</tr>
<tr class="form-row row1 "
id="cultivation_set-2">
<td class="original">
<input type="hidden" name="cultivation_set-2-id" id="id_cultivation_set-2-id" />
<input type="hidden" name="cultivation_set-2-farmer" id="id_cultivation_set-2-farmer" />
</td>
<td class="field-crop">
<select name="cultivation_set-2-crop" id="id_cultivation_set-2-crop">
<option value="" selected="selected">---------</option>
<option value="2">Rice</option>
</select><a href="/admin/bookkeeper/crop/add/" class="add-another" id="add_id_cultivation_set-2-crop" onclick="return showAddAnotherPopup(this);"> <img src="/static/admin/img/icon_addlink.gif" width="10" height="10" alt="Add Another"/></a>
</td>
<td class="field-hectare">
<input type="text" name="cultivation_set-2-hectare" id="id_cultivation_set-2-hectare" />
</td>
<td class="delete"></td>
</tr>
<tr class="form-row row2  empty-form"
id="cultivation_set-empty">
<td class="original">
<input type="hidden" name="cultivation_set-__prefix__-id" id="id_cultivation_set-__prefix__-id" />
<input type="hidden" name="cultivation_set-__prefix__-farmer" id="id_cultivation_set-__prefix__-farmer" />
</td>
<td class="field-crop">
<select name="cultivation_set-__prefix__-crop" id="id_cultivation_set-__prefix__-crop">
<option value="" selected="selected">---------</option>
<option value="2">Rice</option>
</select><a href="/admin/bookkeeper/crop/add/" class="add-another" id="add_id_cultivation_set-__prefix__-crop" onclick="return showAddAnotherPopup(this);"> <img src="/static/admin/img/icon_addlink.gif" width="10" height="10" alt="Add Another"/></a>
</td>
<td class="field-hectare">
<input type="text" name="cultivation_set-__prefix__-hectare" id="id_cultivation_set-__prefix__-hectare" />
</td>
<td class="delete"></td>
</tr>
</tbody>
</table>
</fieldset>
</div>
</div>
<script type="text/javascript">
(function($) {
    $(document).ready(function($) {
        var rows = "#cultivation_set-group .tabular.inline-related tbody tr";
        var alternatingRows = function(row) {
            $(rows).not(".add-row").removeClass("row1 row2")
                .filter(":even").addClass("row1").end()
                .filter(rows + ":odd").addClass("row2");
        }
        var reinitDateTimeShortCuts = function() {
            // Reinitialize the calendar and clock widgets by force
            if (typeof DateTimeShortcuts != "undefined") {
                $(".datetimeshortcuts").remove();
                DateTimeShortcuts.init();
            }
        }
        var updateSelectFilter = function() {
            // If any SelectFilter widgets are a part of the new form,
            // instantiate a new SelectFilter instance for it.
            if (typeof SelectFilter != "undefined"){
                $(".selectfilter").each(function(index, value){
                  var namearr = value.name.split('-');
                  SelectFilter.init(value.id, namearr[namearr.length-1], false, "/static/admin/");
                });
                $(".selectfilterstacked").each(function(index, value){
                  var namearr = value.name.split('-');
                  SelectFilter.init(value.id, namearr[namearr.length-1], true, "/static/admin/");
                });
            }
        }
        var initPrepopulatedFields = function(row) {
            row.find('.prepopulated_field').each(function() {
                var field = $(this);
                var input = field.find('input, select, textarea');
                var dependency_list = input.data('dependency_list') || [];
                var dependencies = [];
                $.each(dependency_list, function(i, field_name) {
                  dependencies.push('#' + row.find('.field-' + field_name).find('input, select, textarea').attr('id'));
                });
                if (dependencies.length) {
                    input.prepopulate(dependencies, input.attr('maxlength'));
                }
            });
        }
        $(rows).formset({
            prefix: "cultivation_set",
            addText: "Add another Cultivation",
            formCssClass: "dynamic-cultivation_set",
            deleteCssClass: "inline-deletelink",
            deleteText: "Remove",
            emptyCssClass: "empty-form",
            removed: alternatingRows,
            added: (function(row) {
                initPrepopulatedFields(row);
                reinitDateTimeShortCuts();
                updateSelectFilter();
                alternatingRows(row);
            })
        });
    });
})(django.jQuery);
</script>
<div class="submit-row">
<input type="submit" value="Save" class="default" name="_save" />
<input type="submit" value="Save and add another" name="_addanother"  />
<input type="submit" value="Save and continue editing" name="_continue" />
</div>
<script type="text/javascript">document.getElementById("id_name").focus();</script>
<script type="text/javascript">
(function($) {
    var field;
})(django.jQuery);
</script>
</div>
</form></div>
