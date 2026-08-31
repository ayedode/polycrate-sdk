from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_projects_partial_update_active_error_component import (
        ApiV1ProjectsPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_annotations_error_component import (
        ApiV1ProjectsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_archived_at_error_component import (
        ApiV1ProjectsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_archived_error_component import (
        ApiV1ProjectsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_archived_reason_error_component import (
        ApiV1ProjectsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_budgeted_hours_error_component import (
        ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_budgeted_hours_interval_error_component import (
        ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_budgeted_hours_mode_error_component import (
        ApiV1ProjectsPartialUpdateBudgetedHoursModeErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_criticality_error_component import (
        ApiV1ProjectsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_debug_mode_error_component import (
        ApiV1ProjectsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_display_name_error_component import (
        ApiV1ProjectsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_end_date_error_component import (
        ApiV1ProjectsPartialUpdateEndDateErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_kind_error_component import (
        ApiV1ProjectsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_labels_error_component import (
        ApiV1ProjectsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_name_error_component import (
        ApiV1ProjectsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_non_field_errors_error_component import (
        ApiV1ProjectsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_organization_id_error_component import (
        ApiV1ProjectsPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_platform_service_error_component import (
        ApiV1ProjectsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_product_id_error_component import (
        ApiV1ProjectsPartialUpdateProductIdErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_provider_error_component import (
        ApiV1ProjectsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_provider_id_error_component import (
        ApiV1ProjectsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_provider_reference_error_component import (
        ApiV1ProjectsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_reconciliation_enabled_error_component import (
        ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_sla_availability_error_component import (
        ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_sla_target_error_component import (
        ApiV1ProjectsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_slo_availability_error_component import (
        ApiV1ProjectsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_slo_target_error_component import (
        ApiV1ProjectsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_start_date_error_component import (
        ApiV1ProjectsPartialUpdateStartDateErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_target_availability_error_component import (
        ApiV1ProjectsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_tolerations_error_component import (
        ApiV1ProjectsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_projects_partial_update_urls_error_component import (
        ApiV1ProjectsPartialUpdateUrlsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProjectsPartialUpdateValidationError")


@_attrs_define
class ApiV1ProjectsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProjectsPartialUpdateActiveErrorComponent |
            ApiV1ProjectsPartialUpdateAnnotationsErrorComponent | ApiV1ProjectsPartialUpdateArchivedAtErrorComponent |
            ApiV1ProjectsPartialUpdateArchivedErrorComponent | ApiV1ProjectsPartialUpdateArchivedReasonErrorComponent |
            ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponent |
            ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponent |
            ApiV1ProjectsPartialUpdateBudgetedHoursModeErrorComponent | ApiV1ProjectsPartialUpdateCriticalityErrorComponent
            | ApiV1ProjectsPartialUpdateDebugModeErrorComponent | ApiV1ProjectsPartialUpdateDisplayNameErrorComponent |
            ApiV1ProjectsPartialUpdateEndDateErrorComponent | ApiV1ProjectsPartialUpdateKindErrorComponent |
            ApiV1ProjectsPartialUpdateLabelsErrorComponent | ApiV1ProjectsPartialUpdateNameErrorComponent |
            ApiV1ProjectsPartialUpdateNonFieldErrorsErrorComponent | ApiV1ProjectsPartialUpdateOrganizationIdErrorComponent
            | ApiV1ProjectsPartialUpdatePlatformServiceErrorComponent | ApiV1ProjectsPartialUpdateProductIdErrorComponent |
            ApiV1ProjectsPartialUpdateProviderErrorComponent | ApiV1ProjectsPartialUpdateProviderIdErrorComponent |
            ApiV1ProjectsPartialUpdateProviderReferenceErrorComponent |
            ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponent | ApiV1ProjectsPartialUpdateSlaTargetErrorComponent |
            ApiV1ProjectsPartialUpdateSloAvailabilityErrorComponent | ApiV1ProjectsPartialUpdateSloTargetErrorComponent |
            ApiV1ProjectsPartialUpdateStartDateErrorComponent | ApiV1ProjectsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1ProjectsPartialUpdateTolerationsErrorComponent | ApiV1ProjectsPartialUpdateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProjectsPartialUpdateActiveErrorComponent
        | ApiV1ProjectsPartialUpdateAnnotationsErrorComponent
        | ApiV1ProjectsPartialUpdateArchivedAtErrorComponent
        | ApiV1ProjectsPartialUpdateArchivedErrorComponent
        | ApiV1ProjectsPartialUpdateArchivedReasonErrorComponent
        | ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponent
        | ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponent
        | ApiV1ProjectsPartialUpdateBudgetedHoursModeErrorComponent
        | ApiV1ProjectsPartialUpdateCriticalityErrorComponent
        | ApiV1ProjectsPartialUpdateDebugModeErrorComponent
        | ApiV1ProjectsPartialUpdateDisplayNameErrorComponent
        | ApiV1ProjectsPartialUpdateEndDateErrorComponent
        | ApiV1ProjectsPartialUpdateKindErrorComponent
        | ApiV1ProjectsPartialUpdateLabelsErrorComponent
        | ApiV1ProjectsPartialUpdateNameErrorComponent
        | ApiV1ProjectsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ProjectsPartialUpdateOrganizationIdErrorComponent
        | ApiV1ProjectsPartialUpdatePlatformServiceErrorComponent
        | ApiV1ProjectsPartialUpdateProductIdErrorComponent
        | ApiV1ProjectsPartialUpdateProviderErrorComponent
        | ApiV1ProjectsPartialUpdateProviderIdErrorComponent
        | ApiV1ProjectsPartialUpdateProviderReferenceErrorComponent
        | ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1ProjectsPartialUpdateSlaTargetErrorComponent
        | ApiV1ProjectsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1ProjectsPartialUpdateSloTargetErrorComponent
        | ApiV1ProjectsPartialUpdateStartDateErrorComponent
        | ApiV1ProjectsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1ProjectsPartialUpdateTolerationsErrorComponent
        | ApiV1ProjectsPartialUpdateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_projects_partial_update_active_error_component import (
            ApiV1ProjectsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_annotations_error_component import (
            ApiV1ProjectsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_archived_at_error_component import (
            ApiV1ProjectsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_archived_error_component import (
            ApiV1ProjectsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_archived_reason_error_component import (
            ApiV1ProjectsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_budgeted_hours_error_component import (
            ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_budgeted_hours_interval_error_component import (
            ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_criticality_error_component import (
            ApiV1ProjectsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_debug_mode_error_component import (
            ApiV1ProjectsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_display_name_error_component import (
            ApiV1ProjectsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_end_date_error_component import (
            ApiV1ProjectsPartialUpdateEndDateErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_kind_error_component import (
            ApiV1ProjectsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_labels_error_component import (
            ApiV1ProjectsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_name_error_component import (
            ApiV1ProjectsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_non_field_errors_error_component import (
            ApiV1ProjectsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_organization_id_error_component import (
            ApiV1ProjectsPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_platform_service_error_component import (
            ApiV1ProjectsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_product_id_error_component import (
            ApiV1ProjectsPartialUpdateProductIdErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_provider_error_component import (
            ApiV1ProjectsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_provider_id_error_component import (
            ApiV1ProjectsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_provider_reference_error_component import (
            ApiV1ProjectsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_reconciliation_enabled_error_component import (
            ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_sla_availability_error_component import (
            ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_sla_target_error_component import (
            ApiV1ProjectsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_slo_availability_error_component import (
            ApiV1ProjectsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_slo_target_error_component import (
            ApiV1ProjectsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_start_date_error_component import (
            ApiV1ProjectsPartialUpdateStartDateErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_target_availability_error_component import (
            ApiV1ProjectsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_tolerations_error_component import (
            ApiV1ProjectsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_urls_error_component import (
            ApiV1ProjectsPartialUpdateUrlsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProjectsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateStartDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateEndDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateProductIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_projects_partial_update_active_error_component import (
            ApiV1ProjectsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_annotations_error_component import (
            ApiV1ProjectsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_archived_at_error_component import (
            ApiV1ProjectsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_archived_error_component import (
            ApiV1ProjectsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_archived_reason_error_component import (
            ApiV1ProjectsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_budgeted_hours_error_component import (
            ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_budgeted_hours_interval_error_component import (
            ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_budgeted_hours_mode_error_component import (
            ApiV1ProjectsPartialUpdateBudgetedHoursModeErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_criticality_error_component import (
            ApiV1ProjectsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_debug_mode_error_component import (
            ApiV1ProjectsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_display_name_error_component import (
            ApiV1ProjectsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_end_date_error_component import (
            ApiV1ProjectsPartialUpdateEndDateErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_kind_error_component import (
            ApiV1ProjectsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_labels_error_component import (
            ApiV1ProjectsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_name_error_component import (
            ApiV1ProjectsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_non_field_errors_error_component import (
            ApiV1ProjectsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_organization_id_error_component import (
            ApiV1ProjectsPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_platform_service_error_component import (
            ApiV1ProjectsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_product_id_error_component import (
            ApiV1ProjectsPartialUpdateProductIdErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_provider_error_component import (
            ApiV1ProjectsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_provider_id_error_component import (
            ApiV1ProjectsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_provider_reference_error_component import (
            ApiV1ProjectsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_reconciliation_enabled_error_component import (
            ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_sla_availability_error_component import (
            ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_sla_target_error_component import (
            ApiV1ProjectsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_slo_availability_error_component import (
            ApiV1ProjectsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_slo_target_error_component import (
            ApiV1ProjectsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_start_date_error_component import (
            ApiV1ProjectsPartialUpdateStartDateErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_target_availability_error_component import (
            ApiV1ProjectsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_tolerations_error_component import (
            ApiV1ProjectsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_projects_partial_update_urls_error_component import (
            ApiV1ProjectsPartialUpdateUrlsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProjectsPartialUpdateActiveErrorComponent
                | ApiV1ProjectsPartialUpdateAnnotationsErrorComponent
                | ApiV1ProjectsPartialUpdateArchivedAtErrorComponent
                | ApiV1ProjectsPartialUpdateArchivedErrorComponent
                | ApiV1ProjectsPartialUpdateArchivedReasonErrorComponent
                | ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponent
                | ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponent
                | ApiV1ProjectsPartialUpdateBudgetedHoursModeErrorComponent
                | ApiV1ProjectsPartialUpdateCriticalityErrorComponent
                | ApiV1ProjectsPartialUpdateDebugModeErrorComponent
                | ApiV1ProjectsPartialUpdateDisplayNameErrorComponent
                | ApiV1ProjectsPartialUpdateEndDateErrorComponent
                | ApiV1ProjectsPartialUpdateKindErrorComponent
                | ApiV1ProjectsPartialUpdateLabelsErrorComponent
                | ApiV1ProjectsPartialUpdateNameErrorComponent
                | ApiV1ProjectsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ProjectsPartialUpdateOrganizationIdErrorComponent
                | ApiV1ProjectsPartialUpdatePlatformServiceErrorComponent
                | ApiV1ProjectsPartialUpdateProductIdErrorComponent
                | ApiV1ProjectsPartialUpdateProviderErrorComponent
                | ApiV1ProjectsPartialUpdateProviderIdErrorComponent
                | ApiV1ProjectsPartialUpdateProviderReferenceErrorComponent
                | ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1ProjectsPartialUpdateSlaTargetErrorComponent
                | ApiV1ProjectsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1ProjectsPartialUpdateSloTargetErrorComponent
                | ApiV1ProjectsPartialUpdateStartDateErrorComponent
                | ApiV1ProjectsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1ProjectsPartialUpdateTolerationsErrorComponent
                | ApiV1ProjectsPartialUpdateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_0 = (
                        ApiV1ProjectsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_1 = (
                        ApiV1ProjectsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_2 = (
                        ApiV1ProjectsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_3 = (
                        ApiV1ProjectsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_4 = (
                        ApiV1ProjectsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_5 = (
                        ApiV1ProjectsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_6 = (
                        ApiV1ProjectsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_7 = (
                        ApiV1ProjectsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_8 = (
                        ApiV1ProjectsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_9 = (
                        ApiV1ProjectsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_10 = (
                        ApiV1ProjectsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_11 = (
                        ApiV1ProjectsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_12 = (
                        ApiV1ProjectsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_13 = (
                        ApiV1ProjectsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_14 = (
                        ApiV1ProjectsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_15 = (
                        ApiV1ProjectsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_16 = (
                        ApiV1ProjectsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_17 = (
                        ApiV1ProjectsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_18 = (
                        ApiV1ProjectsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_19 = (
                        ApiV1ProjectsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_20 = (
                        ApiV1ProjectsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_21 = (
                        ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_22 = (
                        ApiV1ProjectsPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_23 = (
                        ApiV1ProjectsPartialUpdateStartDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_24 = (
                        ApiV1ProjectsPartialUpdateEndDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_25 = (
                        ApiV1ProjectsPartialUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_26 = (
                        ApiV1ProjectsPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_27 = (
                        ApiV1ProjectsPartialUpdateProductIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_28 = (
                        ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_partial_update_error_type_29 = (
                        ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_projects_partial_update_error_type_30 = (
                    ApiV1ProjectsPartialUpdateBudgetedHoursModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_projects_partial_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_projects_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_projects_partial_update_validation_error.additional_properties = d
        return api_v1_projects_partial_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
