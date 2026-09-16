from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_projects_update_active_error_component import ApiV1ProjectsUpdateActiveErrorComponent
    from ..models.api_v1_projects_update_annotations_error_component import ApiV1ProjectsUpdateAnnotationsErrorComponent
    from ..models.api_v1_projects_update_archived_at_error_component import ApiV1ProjectsUpdateArchivedAtErrorComponent
    from ..models.api_v1_projects_update_archived_error_component import ApiV1ProjectsUpdateArchivedErrorComponent
    from ..models.api_v1_projects_update_archived_reason_error_component import (
        ApiV1ProjectsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_projects_update_budgeted_hours_error_component import (
        ApiV1ProjectsUpdateBudgetedHoursErrorComponent,
    )
    from ..models.api_v1_projects_update_budgeted_hours_interval_error_component import (
        ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponent,
    )
    from ..models.api_v1_projects_update_budgeted_hours_mode_error_component import (
        ApiV1ProjectsUpdateBudgetedHoursModeErrorComponent,
    )
    from ..models.api_v1_projects_update_criticality_error_component import ApiV1ProjectsUpdateCriticalityErrorComponent
    from ..models.api_v1_projects_update_debug_mode_error_component import ApiV1ProjectsUpdateDebugModeErrorComponent
    from ..models.api_v1_projects_update_display_name_error_component import (
        ApiV1ProjectsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_projects_update_end_date_error_component import ApiV1ProjectsUpdateEndDateErrorComponent
    from ..models.api_v1_projects_update_kind_error_component import ApiV1ProjectsUpdateKindErrorComponent
    from ..models.api_v1_projects_update_labels_error_component import ApiV1ProjectsUpdateLabelsErrorComponent
    from ..models.api_v1_projects_update_name_error_component import ApiV1ProjectsUpdateNameErrorComponent
    from ..models.api_v1_projects_update_non_field_errors_error_component import (
        ApiV1ProjectsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_projects_update_organization_id_error_component import (
        ApiV1ProjectsUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_projects_update_platform_service_error_component import (
        ApiV1ProjectsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_projects_update_product_id_error_component import ApiV1ProjectsUpdateProductIdErrorComponent
    from ..models.api_v1_projects_update_provider_error_component import ApiV1ProjectsUpdateProviderErrorComponent
    from ..models.api_v1_projects_update_provider_id_error_component import ApiV1ProjectsUpdateProviderIdErrorComponent
    from ..models.api_v1_projects_update_provider_reference_error_component import (
        ApiV1ProjectsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_projects_update_reconciliation_enabled_error_component import (
        ApiV1ProjectsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_projects_update_sla_availability_error_component import (
        ApiV1ProjectsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_update_sla_target_error_component import ApiV1ProjectsUpdateSlaTargetErrorComponent
    from ..models.api_v1_projects_update_slo_availability_error_component import (
        ApiV1ProjectsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_update_slo_target_error_component import ApiV1ProjectsUpdateSloTargetErrorComponent
    from ..models.api_v1_projects_update_start_date_error_component import ApiV1ProjectsUpdateStartDateErrorComponent
    from ..models.api_v1_projects_update_target_availability_error_component import (
        ApiV1ProjectsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_update_tolerations_error_component import ApiV1ProjectsUpdateTolerationsErrorComponent
    from ..models.api_v1_projects_update_urls_error_component import ApiV1ProjectsUpdateUrlsErrorComponent


T = TypeVar("T", bound="ApiV1ProjectsUpdateValidationError")


@_attrs_define
class ApiV1ProjectsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProjectsUpdateActiveErrorComponent | ApiV1ProjectsUpdateAnnotationsErrorComponent |
            ApiV1ProjectsUpdateArchivedAtErrorComponent | ApiV1ProjectsUpdateArchivedErrorComponent |
            ApiV1ProjectsUpdateArchivedReasonErrorComponent | ApiV1ProjectsUpdateBudgetedHoursErrorComponent |
            ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponent | ApiV1ProjectsUpdateBudgetedHoursModeErrorComponent |
            ApiV1ProjectsUpdateCriticalityErrorComponent | ApiV1ProjectsUpdateDebugModeErrorComponent |
            ApiV1ProjectsUpdateDisplayNameErrorComponent | ApiV1ProjectsUpdateEndDateErrorComponent |
            ApiV1ProjectsUpdateKindErrorComponent | ApiV1ProjectsUpdateLabelsErrorComponent |
            ApiV1ProjectsUpdateNameErrorComponent | ApiV1ProjectsUpdateNonFieldErrorsErrorComponent |
            ApiV1ProjectsUpdateOrganizationIdErrorComponent | ApiV1ProjectsUpdatePlatformServiceErrorComponent |
            ApiV1ProjectsUpdateProductIdErrorComponent | ApiV1ProjectsUpdateProviderErrorComponent |
            ApiV1ProjectsUpdateProviderIdErrorComponent | ApiV1ProjectsUpdateProviderReferenceErrorComponent |
            ApiV1ProjectsUpdateReconciliationEnabledErrorComponent | ApiV1ProjectsUpdateSlaAvailabilityErrorComponent |
            ApiV1ProjectsUpdateSlaTargetErrorComponent | ApiV1ProjectsUpdateSloAvailabilityErrorComponent |
            ApiV1ProjectsUpdateSloTargetErrorComponent | ApiV1ProjectsUpdateStartDateErrorComponent |
            ApiV1ProjectsUpdateTargetAvailabilityErrorComponent | ApiV1ProjectsUpdateTolerationsErrorComponent |
            ApiV1ProjectsUpdateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProjectsUpdateActiveErrorComponent
        | ApiV1ProjectsUpdateAnnotationsErrorComponent
        | ApiV1ProjectsUpdateArchivedAtErrorComponent
        | ApiV1ProjectsUpdateArchivedErrorComponent
        | ApiV1ProjectsUpdateArchivedReasonErrorComponent
        | ApiV1ProjectsUpdateBudgetedHoursErrorComponent
        | ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponent
        | ApiV1ProjectsUpdateBudgetedHoursModeErrorComponent
        | ApiV1ProjectsUpdateCriticalityErrorComponent
        | ApiV1ProjectsUpdateDebugModeErrorComponent
        | ApiV1ProjectsUpdateDisplayNameErrorComponent
        | ApiV1ProjectsUpdateEndDateErrorComponent
        | ApiV1ProjectsUpdateKindErrorComponent
        | ApiV1ProjectsUpdateLabelsErrorComponent
        | ApiV1ProjectsUpdateNameErrorComponent
        | ApiV1ProjectsUpdateNonFieldErrorsErrorComponent
        | ApiV1ProjectsUpdateOrganizationIdErrorComponent
        | ApiV1ProjectsUpdatePlatformServiceErrorComponent
        | ApiV1ProjectsUpdateProductIdErrorComponent
        | ApiV1ProjectsUpdateProviderErrorComponent
        | ApiV1ProjectsUpdateProviderIdErrorComponent
        | ApiV1ProjectsUpdateProviderReferenceErrorComponent
        | ApiV1ProjectsUpdateReconciliationEnabledErrorComponent
        | ApiV1ProjectsUpdateSlaAvailabilityErrorComponent
        | ApiV1ProjectsUpdateSlaTargetErrorComponent
        | ApiV1ProjectsUpdateSloAvailabilityErrorComponent
        | ApiV1ProjectsUpdateSloTargetErrorComponent
        | ApiV1ProjectsUpdateStartDateErrorComponent
        | ApiV1ProjectsUpdateTargetAvailabilityErrorComponent
        | ApiV1ProjectsUpdateTolerationsErrorComponent
        | ApiV1ProjectsUpdateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_projects_update_active_error_component import (
            ApiV1ProjectsUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_annotations_error_component import (
            ApiV1ProjectsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_archived_at_error_component import (
            ApiV1ProjectsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_archived_error_component import (
            ApiV1ProjectsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_archived_reason_error_component import (
            ApiV1ProjectsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_budgeted_hours_error_component import (
            ApiV1ProjectsUpdateBudgetedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_budgeted_hours_interval_error_component import (
            ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_criticality_error_component import (
            ApiV1ProjectsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_debug_mode_error_component import (
            ApiV1ProjectsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_display_name_error_component import (
            ApiV1ProjectsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_end_date_error_component import (
            ApiV1ProjectsUpdateEndDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_kind_error_component import (
            ApiV1ProjectsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_labels_error_component import (
            ApiV1ProjectsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_name_error_component import (
            ApiV1ProjectsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_non_field_errors_error_component import (
            ApiV1ProjectsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_organization_id_error_component import (
            ApiV1ProjectsUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_platform_service_error_component import (
            ApiV1ProjectsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_product_id_error_component import (
            ApiV1ProjectsUpdateProductIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_provider_error_component import (
            ApiV1ProjectsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_provider_id_error_component import (
            ApiV1ProjectsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_provider_reference_error_component import (
            ApiV1ProjectsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_reconciliation_enabled_error_component import (
            ApiV1ProjectsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_sla_availability_error_component import (
            ApiV1ProjectsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_sla_target_error_component import (
            ApiV1ProjectsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_slo_availability_error_component import (
            ApiV1ProjectsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_slo_target_error_component import (
            ApiV1ProjectsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_start_date_error_component import (
            ApiV1ProjectsUpdateStartDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_target_availability_error_component import (
            ApiV1ProjectsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_tolerations_error_component import (
            ApiV1ProjectsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_urls_error_component import (
            ApiV1ProjectsUpdateUrlsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProjectsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateStartDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateEndDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateProductIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateBudgetedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponent):
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
        from ..models.api_v1_projects_update_active_error_component import (
            ApiV1ProjectsUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_annotations_error_component import (
            ApiV1ProjectsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_archived_at_error_component import (
            ApiV1ProjectsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_archived_error_component import (
            ApiV1ProjectsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_archived_reason_error_component import (
            ApiV1ProjectsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_budgeted_hours_error_component import (
            ApiV1ProjectsUpdateBudgetedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_budgeted_hours_interval_error_component import (
            ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_budgeted_hours_mode_error_component import (
            ApiV1ProjectsUpdateBudgetedHoursModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_criticality_error_component import (
            ApiV1ProjectsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_debug_mode_error_component import (
            ApiV1ProjectsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_display_name_error_component import (
            ApiV1ProjectsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_end_date_error_component import (
            ApiV1ProjectsUpdateEndDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_kind_error_component import (
            ApiV1ProjectsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_labels_error_component import (
            ApiV1ProjectsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_name_error_component import (
            ApiV1ProjectsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_non_field_errors_error_component import (
            ApiV1ProjectsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_organization_id_error_component import (
            ApiV1ProjectsUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_platform_service_error_component import (
            ApiV1ProjectsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_product_id_error_component import (
            ApiV1ProjectsUpdateProductIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_provider_error_component import (
            ApiV1ProjectsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_provider_id_error_component import (
            ApiV1ProjectsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_provider_reference_error_component import (
            ApiV1ProjectsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_reconciliation_enabled_error_component import (
            ApiV1ProjectsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_sla_availability_error_component import (
            ApiV1ProjectsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_sla_target_error_component import (
            ApiV1ProjectsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_slo_availability_error_component import (
            ApiV1ProjectsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_slo_target_error_component import (
            ApiV1ProjectsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_start_date_error_component import (
            ApiV1ProjectsUpdateStartDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_target_availability_error_component import (
            ApiV1ProjectsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_tolerations_error_component import (
            ApiV1ProjectsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_update_urls_error_component import (
            ApiV1ProjectsUpdateUrlsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProjectsUpdateActiveErrorComponent
                | ApiV1ProjectsUpdateAnnotationsErrorComponent
                | ApiV1ProjectsUpdateArchivedAtErrorComponent
                | ApiV1ProjectsUpdateArchivedErrorComponent
                | ApiV1ProjectsUpdateArchivedReasonErrorComponent
                | ApiV1ProjectsUpdateBudgetedHoursErrorComponent
                | ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponent
                | ApiV1ProjectsUpdateBudgetedHoursModeErrorComponent
                | ApiV1ProjectsUpdateCriticalityErrorComponent
                | ApiV1ProjectsUpdateDebugModeErrorComponent
                | ApiV1ProjectsUpdateDisplayNameErrorComponent
                | ApiV1ProjectsUpdateEndDateErrorComponent
                | ApiV1ProjectsUpdateKindErrorComponent
                | ApiV1ProjectsUpdateLabelsErrorComponent
                | ApiV1ProjectsUpdateNameErrorComponent
                | ApiV1ProjectsUpdateNonFieldErrorsErrorComponent
                | ApiV1ProjectsUpdateOrganizationIdErrorComponent
                | ApiV1ProjectsUpdatePlatformServiceErrorComponent
                | ApiV1ProjectsUpdateProductIdErrorComponent
                | ApiV1ProjectsUpdateProviderErrorComponent
                | ApiV1ProjectsUpdateProviderIdErrorComponent
                | ApiV1ProjectsUpdateProviderReferenceErrorComponent
                | ApiV1ProjectsUpdateReconciliationEnabledErrorComponent
                | ApiV1ProjectsUpdateSlaAvailabilityErrorComponent
                | ApiV1ProjectsUpdateSlaTargetErrorComponent
                | ApiV1ProjectsUpdateSloAvailabilityErrorComponent
                | ApiV1ProjectsUpdateSloTargetErrorComponent
                | ApiV1ProjectsUpdateStartDateErrorComponent
                | ApiV1ProjectsUpdateTargetAvailabilityErrorComponent
                | ApiV1ProjectsUpdateTolerationsErrorComponent
                | ApiV1ProjectsUpdateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_0 = (
                        ApiV1ProjectsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_1 = (
                        ApiV1ProjectsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_2 = (
                        ApiV1ProjectsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_3 = (
                        ApiV1ProjectsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_4 = (
                        ApiV1ProjectsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_5 = (
                        ApiV1ProjectsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_6 = (
                        ApiV1ProjectsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_7 = (
                        ApiV1ProjectsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_8 = (
                        ApiV1ProjectsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_9 = (
                        ApiV1ProjectsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_10 = (
                        ApiV1ProjectsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_11 = (
                        ApiV1ProjectsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_12 = (
                        ApiV1ProjectsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_13 = (
                        ApiV1ProjectsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_14 = (
                        ApiV1ProjectsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_15 = (
                        ApiV1ProjectsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_16 = (
                        ApiV1ProjectsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_17 = (
                        ApiV1ProjectsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_18 = (
                        ApiV1ProjectsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_19 = (
                        ApiV1ProjectsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_20 = (
                        ApiV1ProjectsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_21 = (
                        ApiV1ProjectsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_22 = (
                        ApiV1ProjectsUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_23 = (
                        ApiV1ProjectsUpdateStartDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_24 = (
                        ApiV1ProjectsUpdateEndDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_25 = (
                        ApiV1ProjectsUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_26 = (
                        ApiV1ProjectsUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_27 = (
                        ApiV1ProjectsUpdateProductIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_28 = (
                        ApiV1ProjectsUpdateBudgetedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_update_error_type_29 = (
                        ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_projects_update_error_type_30 = (
                    ApiV1ProjectsUpdateBudgetedHoursModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_projects_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_projects_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_projects_update_validation_error.additional_properties = d
        return api_v1_projects_update_validation_error

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
