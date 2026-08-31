from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_projects_archive_create_active_error_component import (
        ApiV1ProjectsArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_annotations_error_component import (
        ApiV1ProjectsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_archived_at_error_component import (
        ApiV1ProjectsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_archived_error_component import (
        ApiV1ProjectsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_archived_reason_error_component import (
        ApiV1ProjectsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_budgeted_hours_error_component import (
        ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_budgeted_hours_interval_error_component import (
        ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_budgeted_hours_mode_error_component import (
        ApiV1ProjectsArchiveCreateBudgetedHoursModeErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_criticality_error_component import (
        ApiV1ProjectsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_debug_mode_error_component import (
        ApiV1ProjectsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_display_name_error_component import (
        ApiV1ProjectsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_end_date_error_component import (
        ApiV1ProjectsArchiveCreateEndDateErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_kind_error_component import (
        ApiV1ProjectsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_labels_error_component import (
        ApiV1ProjectsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_name_error_component import (
        ApiV1ProjectsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_non_field_errors_error_component import (
        ApiV1ProjectsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_organization_id_error_component import (
        ApiV1ProjectsArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_platform_service_error_component import (
        ApiV1ProjectsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_product_id_error_component import (
        ApiV1ProjectsArchiveCreateProductIdErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_provider_error_component import (
        ApiV1ProjectsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_provider_id_error_component import (
        ApiV1ProjectsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_provider_reference_error_component import (
        ApiV1ProjectsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_reconciliation_enabled_error_component import (
        ApiV1ProjectsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_sla_availability_error_component import (
        ApiV1ProjectsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_sla_target_error_component import (
        ApiV1ProjectsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_slo_availability_error_component import (
        ApiV1ProjectsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_slo_target_error_component import (
        ApiV1ProjectsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_start_date_error_component import (
        ApiV1ProjectsArchiveCreateStartDateErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_target_availability_error_component import (
        ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_tolerations_error_component import (
        ApiV1ProjectsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_projects_archive_create_urls_error_component import (
        ApiV1ProjectsArchiveCreateUrlsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProjectsArchiveCreateValidationError")


@_attrs_define
class ApiV1ProjectsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProjectsArchiveCreateActiveErrorComponent |
            ApiV1ProjectsArchiveCreateAnnotationsErrorComponent | ApiV1ProjectsArchiveCreateArchivedAtErrorComponent |
            ApiV1ProjectsArchiveCreateArchivedErrorComponent | ApiV1ProjectsArchiveCreateArchivedReasonErrorComponent |
            ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponent |
            ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponent |
            ApiV1ProjectsArchiveCreateBudgetedHoursModeErrorComponent | ApiV1ProjectsArchiveCreateCriticalityErrorComponent
            | ApiV1ProjectsArchiveCreateDebugModeErrorComponent | ApiV1ProjectsArchiveCreateDisplayNameErrorComponent |
            ApiV1ProjectsArchiveCreateEndDateErrorComponent | ApiV1ProjectsArchiveCreateKindErrorComponent |
            ApiV1ProjectsArchiveCreateLabelsErrorComponent | ApiV1ProjectsArchiveCreateNameErrorComponent |
            ApiV1ProjectsArchiveCreateNonFieldErrorsErrorComponent | ApiV1ProjectsArchiveCreateOrganizationIdErrorComponent
            | ApiV1ProjectsArchiveCreatePlatformServiceErrorComponent | ApiV1ProjectsArchiveCreateProductIdErrorComponent |
            ApiV1ProjectsArchiveCreateProviderErrorComponent | ApiV1ProjectsArchiveCreateProviderIdErrorComponent |
            ApiV1ProjectsArchiveCreateProviderReferenceErrorComponent |
            ApiV1ProjectsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1ProjectsArchiveCreateSlaAvailabilityErrorComponent | ApiV1ProjectsArchiveCreateSlaTargetErrorComponent |
            ApiV1ProjectsArchiveCreateSloAvailabilityErrorComponent | ApiV1ProjectsArchiveCreateSloTargetErrorComponent |
            ApiV1ProjectsArchiveCreateStartDateErrorComponent | ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ProjectsArchiveCreateTolerationsErrorComponent | ApiV1ProjectsArchiveCreateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProjectsArchiveCreateActiveErrorComponent
        | ApiV1ProjectsArchiveCreateAnnotationsErrorComponent
        | ApiV1ProjectsArchiveCreateArchivedAtErrorComponent
        | ApiV1ProjectsArchiveCreateArchivedErrorComponent
        | ApiV1ProjectsArchiveCreateArchivedReasonErrorComponent
        | ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponent
        | ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponent
        | ApiV1ProjectsArchiveCreateBudgetedHoursModeErrorComponent
        | ApiV1ProjectsArchiveCreateCriticalityErrorComponent
        | ApiV1ProjectsArchiveCreateDebugModeErrorComponent
        | ApiV1ProjectsArchiveCreateDisplayNameErrorComponent
        | ApiV1ProjectsArchiveCreateEndDateErrorComponent
        | ApiV1ProjectsArchiveCreateKindErrorComponent
        | ApiV1ProjectsArchiveCreateLabelsErrorComponent
        | ApiV1ProjectsArchiveCreateNameErrorComponent
        | ApiV1ProjectsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ProjectsArchiveCreateOrganizationIdErrorComponent
        | ApiV1ProjectsArchiveCreatePlatformServiceErrorComponent
        | ApiV1ProjectsArchiveCreateProductIdErrorComponent
        | ApiV1ProjectsArchiveCreateProviderErrorComponent
        | ApiV1ProjectsArchiveCreateProviderIdErrorComponent
        | ApiV1ProjectsArchiveCreateProviderReferenceErrorComponent
        | ApiV1ProjectsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ProjectsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ProjectsArchiveCreateSlaTargetErrorComponent
        | ApiV1ProjectsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ProjectsArchiveCreateSloTargetErrorComponent
        | ApiV1ProjectsArchiveCreateStartDateErrorComponent
        | ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ProjectsArchiveCreateTolerationsErrorComponent
        | ApiV1ProjectsArchiveCreateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_projects_archive_create_active_error_component import (
            ApiV1ProjectsArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_annotations_error_component import (
            ApiV1ProjectsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_archived_at_error_component import (
            ApiV1ProjectsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_archived_error_component import (
            ApiV1ProjectsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_archived_reason_error_component import (
            ApiV1ProjectsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_budgeted_hours_error_component import (
            ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_budgeted_hours_interval_error_component import (
            ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_criticality_error_component import (
            ApiV1ProjectsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_debug_mode_error_component import (
            ApiV1ProjectsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_display_name_error_component import (
            ApiV1ProjectsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_end_date_error_component import (
            ApiV1ProjectsArchiveCreateEndDateErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_kind_error_component import (
            ApiV1ProjectsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_labels_error_component import (
            ApiV1ProjectsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_name_error_component import (
            ApiV1ProjectsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_non_field_errors_error_component import (
            ApiV1ProjectsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_organization_id_error_component import (
            ApiV1ProjectsArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_platform_service_error_component import (
            ApiV1ProjectsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_product_id_error_component import (
            ApiV1ProjectsArchiveCreateProductIdErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_provider_error_component import (
            ApiV1ProjectsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_provider_id_error_component import (
            ApiV1ProjectsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_provider_reference_error_component import (
            ApiV1ProjectsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_reconciliation_enabled_error_component import (
            ApiV1ProjectsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_sla_availability_error_component import (
            ApiV1ProjectsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_sla_target_error_component import (
            ApiV1ProjectsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_slo_availability_error_component import (
            ApiV1ProjectsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_slo_target_error_component import (
            ApiV1ProjectsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_start_date_error_component import (
            ApiV1ProjectsArchiveCreateStartDateErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_target_availability_error_component import (
            ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_tolerations_error_component import (
            ApiV1ProjectsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_urls_error_component import (
            ApiV1ProjectsArchiveCreateUrlsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProjectsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateStartDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateEndDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateProductIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponent):
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
        from ..models.api_v1_projects_archive_create_active_error_component import (
            ApiV1ProjectsArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_annotations_error_component import (
            ApiV1ProjectsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_archived_at_error_component import (
            ApiV1ProjectsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_archived_error_component import (
            ApiV1ProjectsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_archived_reason_error_component import (
            ApiV1ProjectsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_budgeted_hours_error_component import (
            ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_budgeted_hours_interval_error_component import (
            ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_budgeted_hours_mode_error_component import (
            ApiV1ProjectsArchiveCreateBudgetedHoursModeErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_criticality_error_component import (
            ApiV1ProjectsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_debug_mode_error_component import (
            ApiV1ProjectsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_display_name_error_component import (
            ApiV1ProjectsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_end_date_error_component import (
            ApiV1ProjectsArchiveCreateEndDateErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_kind_error_component import (
            ApiV1ProjectsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_labels_error_component import (
            ApiV1ProjectsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_name_error_component import (
            ApiV1ProjectsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_non_field_errors_error_component import (
            ApiV1ProjectsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_organization_id_error_component import (
            ApiV1ProjectsArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_platform_service_error_component import (
            ApiV1ProjectsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_product_id_error_component import (
            ApiV1ProjectsArchiveCreateProductIdErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_provider_error_component import (
            ApiV1ProjectsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_provider_id_error_component import (
            ApiV1ProjectsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_provider_reference_error_component import (
            ApiV1ProjectsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_reconciliation_enabled_error_component import (
            ApiV1ProjectsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_sla_availability_error_component import (
            ApiV1ProjectsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_sla_target_error_component import (
            ApiV1ProjectsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_slo_availability_error_component import (
            ApiV1ProjectsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_slo_target_error_component import (
            ApiV1ProjectsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_start_date_error_component import (
            ApiV1ProjectsArchiveCreateStartDateErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_target_availability_error_component import (
            ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_tolerations_error_component import (
            ApiV1ProjectsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_projects_archive_create_urls_error_component import (
            ApiV1ProjectsArchiveCreateUrlsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProjectsArchiveCreateActiveErrorComponent
                | ApiV1ProjectsArchiveCreateAnnotationsErrorComponent
                | ApiV1ProjectsArchiveCreateArchivedAtErrorComponent
                | ApiV1ProjectsArchiveCreateArchivedErrorComponent
                | ApiV1ProjectsArchiveCreateArchivedReasonErrorComponent
                | ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponent
                | ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponent
                | ApiV1ProjectsArchiveCreateBudgetedHoursModeErrorComponent
                | ApiV1ProjectsArchiveCreateCriticalityErrorComponent
                | ApiV1ProjectsArchiveCreateDebugModeErrorComponent
                | ApiV1ProjectsArchiveCreateDisplayNameErrorComponent
                | ApiV1ProjectsArchiveCreateEndDateErrorComponent
                | ApiV1ProjectsArchiveCreateKindErrorComponent
                | ApiV1ProjectsArchiveCreateLabelsErrorComponent
                | ApiV1ProjectsArchiveCreateNameErrorComponent
                | ApiV1ProjectsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ProjectsArchiveCreateOrganizationIdErrorComponent
                | ApiV1ProjectsArchiveCreatePlatformServiceErrorComponent
                | ApiV1ProjectsArchiveCreateProductIdErrorComponent
                | ApiV1ProjectsArchiveCreateProviderErrorComponent
                | ApiV1ProjectsArchiveCreateProviderIdErrorComponent
                | ApiV1ProjectsArchiveCreateProviderReferenceErrorComponent
                | ApiV1ProjectsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ProjectsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ProjectsArchiveCreateSlaTargetErrorComponent
                | ApiV1ProjectsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ProjectsArchiveCreateSloTargetErrorComponent
                | ApiV1ProjectsArchiveCreateStartDateErrorComponent
                | ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ProjectsArchiveCreateTolerationsErrorComponent
                | ApiV1ProjectsArchiveCreateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_0 = (
                        ApiV1ProjectsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_1 = (
                        ApiV1ProjectsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_2 = (
                        ApiV1ProjectsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_3 = (
                        ApiV1ProjectsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_4 = (
                        ApiV1ProjectsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_5 = (
                        ApiV1ProjectsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_6 = (
                        ApiV1ProjectsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_7 = (
                        ApiV1ProjectsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_8 = (
                        ApiV1ProjectsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_9 = (
                        ApiV1ProjectsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_10 = (
                        ApiV1ProjectsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_11 = (
                        ApiV1ProjectsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_12 = (
                        ApiV1ProjectsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_13 = (
                        ApiV1ProjectsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_14 = (
                        ApiV1ProjectsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_15 = (
                        ApiV1ProjectsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_16 = (
                        ApiV1ProjectsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_17 = (
                        ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_18 = (
                        ApiV1ProjectsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_19 = (
                        ApiV1ProjectsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_20 = (
                        ApiV1ProjectsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_21 = (
                        ApiV1ProjectsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_22 = (
                        ApiV1ProjectsArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_23 = (
                        ApiV1ProjectsArchiveCreateStartDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_24 = (
                        ApiV1ProjectsArchiveCreateEndDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_25 = (
                        ApiV1ProjectsArchiveCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_26 = (
                        ApiV1ProjectsArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_27 = (
                        ApiV1ProjectsArchiveCreateProductIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_28 = (
                        ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_archive_create_error_type_29 = (
                        ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_projects_archive_create_error_type_30 = (
                    ApiV1ProjectsArchiveCreateBudgetedHoursModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_projects_archive_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_projects_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_projects_archive_create_validation_error.additional_properties = d
        return api_v1_projects_archive_create_validation_error

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
