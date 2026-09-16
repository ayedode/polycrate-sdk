from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_projects_create_active_error_component import ApiV1ProjectsCreateActiveErrorComponent
    from ..models.api_v1_projects_create_annotations_error_component import ApiV1ProjectsCreateAnnotationsErrorComponent
    from ..models.api_v1_projects_create_archived_at_error_component import ApiV1ProjectsCreateArchivedAtErrorComponent
    from ..models.api_v1_projects_create_archived_error_component import ApiV1ProjectsCreateArchivedErrorComponent
    from ..models.api_v1_projects_create_archived_reason_error_component import (
        ApiV1ProjectsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_projects_create_budgeted_hours_error_component import (
        ApiV1ProjectsCreateBudgetedHoursErrorComponent,
    )
    from ..models.api_v1_projects_create_budgeted_hours_interval_error_component import (
        ApiV1ProjectsCreateBudgetedHoursIntervalErrorComponent,
    )
    from ..models.api_v1_projects_create_budgeted_hours_mode_error_component import (
        ApiV1ProjectsCreateBudgetedHoursModeErrorComponent,
    )
    from ..models.api_v1_projects_create_criticality_error_component import ApiV1ProjectsCreateCriticalityErrorComponent
    from ..models.api_v1_projects_create_debug_mode_error_component import ApiV1ProjectsCreateDebugModeErrorComponent
    from ..models.api_v1_projects_create_display_name_error_component import (
        ApiV1ProjectsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_projects_create_end_date_error_component import ApiV1ProjectsCreateEndDateErrorComponent
    from ..models.api_v1_projects_create_kind_error_component import ApiV1ProjectsCreateKindErrorComponent
    from ..models.api_v1_projects_create_labels_error_component import ApiV1ProjectsCreateLabelsErrorComponent
    from ..models.api_v1_projects_create_name_error_component import ApiV1ProjectsCreateNameErrorComponent
    from ..models.api_v1_projects_create_non_field_errors_error_component import (
        ApiV1ProjectsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_projects_create_organization_id_error_component import (
        ApiV1ProjectsCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_projects_create_platform_service_error_component import (
        ApiV1ProjectsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_projects_create_product_id_error_component import ApiV1ProjectsCreateProductIdErrorComponent
    from ..models.api_v1_projects_create_provider_error_component import ApiV1ProjectsCreateProviderErrorComponent
    from ..models.api_v1_projects_create_provider_id_error_component import ApiV1ProjectsCreateProviderIdErrorComponent
    from ..models.api_v1_projects_create_provider_reference_error_component import (
        ApiV1ProjectsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_projects_create_reconciliation_enabled_error_component import (
        ApiV1ProjectsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_projects_create_sla_availability_error_component import (
        ApiV1ProjectsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_create_sla_target_error_component import ApiV1ProjectsCreateSlaTargetErrorComponent
    from ..models.api_v1_projects_create_slo_availability_error_component import (
        ApiV1ProjectsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_create_slo_target_error_component import ApiV1ProjectsCreateSloTargetErrorComponent
    from ..models.api_v1_projects_create_start_date_error_component import ApiV1ProjectsCreateStartDateErrorComponent
    from ..models.api_v1_projects_create_target_availability_error_component import (
        ApiV1ProjectsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_projects_create_tolerations_error_component import ApiV1ProjectsCreateTolerationsErrorComponent
    from ..models.api_v1_projects_create_urls_error_component import ApiV1ProjectsCreateUrlsErrorComponent


T = TypeVar("T", bound="ApiV1ProjectsCreateValidationError")


@_attrs_define
class ApiV1ProjectsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProjectsCreateActiveErrorComponent | ApiV1ProjectsCreateAnnotationsErrorComponent |
            ApiV1ProjectsCreateArchivedAtErrorComponent | ApiV1ProjectsCreateArchivedErrorComponent |
            ApiV1ProjectsCreateArchivedReasonErrorComponent | ApiV1ProjectsCreateBudgetedHoursErrorComponent |
            ApiV1ProjectsCreateBudgetedHoursIntervalErrorComponent | ApiV1ProjectsCreateBudgetedHoursModeErrorComponent |
            ApiV1ProjectsCreateCriticalityErrorComponent | ApiV1ProjectsCreateDebugModeErrorComponent |
            ApiV1ProjectsCreateDisplayNameErrorComponent | ApiV1ProjectsCreateEndDateErrorComponent |
            ApiV1ProjectsCreateKindErrorComponent | ApiV1ProjectsCreateLabelsErrorComponent |
            ApiV1ProjectsCreateNameErrorComponent | ApiV1ProjectsCreateNonFieldErrorsErrorComponent |
            ApiV1ProjectsCreateOrganizationIdErrorComponent | ApiV1ProjectsCreatePlatformServiceErrorComponent |
            ApiV1ProjectsCreateProductIdErrorComponent | ApiV1ProjectsCreateProviderErrorComponent |
            ApiV1ProjectsCreateProviderIdErrorComponent | ApiV1ProjectsCreateProviderReferenceErrorComponent |
            ApiV1ProjectsCreateReconciliationEnabledErrorComponent | ApiV1ProjectsCreateSlaAvailabilityErrorComponent |
            ApiV1ProjectsCreateSlaTargetErrorComponent | ApiV1ProjectsCreateSloAvailabilityErrorComponent |
            ApiV1ProjectsCreateSloTargetErrorComponent | ApiV1ProjectsCreateStartDateErrorComponent |
            ApiV1ProjectsCreateTargetAvailabilityErrorComponent | ApiV1ProjectsCreateTolerationsErrorComponent |
            ApiV1ProjectsCreateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProjectsCreateActiveErrorComponent
        | ApiV1ProjectsCreateAnnotationsErrorComponent
        | ApiV1ProjectsCreateArchivedAtErrorComponent
        | ApiV1ProjectsCreateArchivedErrorComponent
        | ApiV1ProjectsCreateArchivedReasonErrorComponent
        | ApiV1ProjectsCreateBudgetedHoursErrorComponent
        | ApiV1ProjectsCreateBudgetedHoursIntervalErrorComponent
        | ApiV1ProjectsCreateBudgetedHoursModeErrorComponent
        | ApiV1ProjectsCreateCriticalityErrorComponent
        | ApiV1ProjectsCreateDebugModeErrorComponent
        | ApiV1ProjectsCreateDisplayNameErrorComponent
        | ApiV1ProjectsCreateEndDateErrorComponent
        | ApiV1ProjectsCreateKindErrorComponent
        | ApiV1ProjectsCreateLabelsErrorComponent
        | ApiV1ProjectsCreateNameErrorComponent
        | ApiV1ProjectsCreateNonFieldErrorsErrorComponent
        | ApiV1ProjectsCreateOrganizationIdErrorComponent
        | ApiV1ProjectsCreatePlatformServiceErrorComponent
        | ApiV1ProjectsCreateProductIdErrorComponent
        | ApiV1ProjectsCreateProviderErrorComponent
        | ApiV1ProjectsCreateProviderIdErrorComponent
        | ApiV1ProjectsCreateProviderReferenceErrorComponent
        | ApiV1ProjectsCreateReconciliationEnabledErrorComponent
        | ApiV1ProjectsCreateSlaAvailabilityErrorComponent
        | ApiV1ProjectsCreateSlaTargetErrorComponent
        | ApiV1ProjectsCreateSloAvailabilityErrorComponent
        | ApiV1ProjectsCreateSloTargetErrorComponent
        | ApiV1ProjectsCreateStartDateErrorComponent
        | ApiV1ProjectsCreateTargetAvailabilityErrorComponent
        | ApiV1ProjectsCreateTolerationsErrorComponent
        | ApiV1ProjectsCreateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_projects_create_active_error_component import (
            ApiV1ProjectsCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_annotations_error_component import (
            ApiV1ProjectsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_archived_at_error_component import (
            ApiV1ProjectsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_archived_error_component import (
            ApiV1ProjectsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_archived_reason_error_component import (
            ApiV1ProjectsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_budgeted_hours_error_component import (
            ApiV1ProjectsCreateBudgetedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_budgeted_hours_interval_error_component import (
            ApiV1ProjectsCreateBudgetedHoursIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_criticality_error_component import (
            ApiV1ProjectsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_debug_mode_error_component import (
            ApiV1ProjectsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_display_name_error_component import (
            ApiV1ProjectsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_end_date_error_component import (
            ApiV1ProjectsCreateEndDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_kind_error_component import (
            ApiV1ProjectsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_labels_error_component import (
            ApiV1ProjectsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_name_error_component import (
            ApiV1ProjectsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_non_field_errors_error_component import (
            ApiV1ProjectsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_organization_id_error_component import (
            ApiV1ProjectsCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_platform_service_error_component import (
            ApiV1ProjectsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_product_id_error_component import (
            ApiV1ProjectsCreateProductIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_provider_error_component import (
            ApiV1ProjectsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_provider_id_error_component import (
            ApiV1ProjectsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_provider_reference_error_component import (
            ApiV1ProjectsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_reconciliation_enabled_error_component import (
            ApiV1ProjectsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_sla_availability_error_component import (
            ApiV1ProjectsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_sla_target_error_component import (
            ApiV1ProjectsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_slo_availability_error_component import (
            ApiV1ProjectsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_slo_target_error_component import (
            ApiV1ProjectsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_start_date_error_component import (
            ApiV1ProjectsCreateStartDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_target_availability_error_component import (
            ApiV1ProjectsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_tolerations_error_component import (
            ApiV1ProjectsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_urls_error_component import (
            ApiV1ProjectsCreateUrlsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProjectsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateStartDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateEndDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateProductIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateBudgetedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProjectsCreateBudgetedHoursIntervalErrorComponent):
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
        from ..models.api_v1_projects_create_active_error_component import (
            ApiV1ProjectsCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_annotations_error_component import (
            ApiV1ProjectsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_archived_at_error_component import (
            ApiV1ProjectsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_archived_error_component import (
            ApiV1ProjectsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_archived_reason_error_component import (
            ApiV1ProjectsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_budgeted_hours_error_component import (
            ApiV1ProjectsCreateBudgetedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_budgeted_hours_interval_error_component import (
            ApiV1ProjectsCreateBudgetedHoursIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_budgeted_hours_mode_error_component import (
            ApiV1ProjectsCreateBudgetedHoursModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_criticality_error_component import (
            ApiV1ProjectsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_debug_mode_error_component import (
            ApiV1ProjectsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_display_name_error_component import (
            ApiV1ProjectsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_end_date_error_component import (
            ApiV1ProjectsCreateEndDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_kind_error_component import (
            ApiV1ProjectsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_labels_error_component import (
            ApiV1ProjectsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_name_error_component import (
            ApiV1ProjectsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_non_field_errors_error_component import (
            ApiV1ProjectsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_organization_id_error_component import (
            ApiV1ProjectsCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_platform_service_error_component import (
            ApiV1ProjectsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_product_id_error_component import (
            ApiV1ProjectsCreateProductIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_provider_error_component import (
            ApiV1ProjectsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_provider_id_error_component import (
            ApiV1ProjectsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_provider_reference_error_component import (
            ApiV1ProjectsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_reconciliation_enabled_error_component import (
            ApiV1ProjectsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_sla_availability_error_component import (
            ApiV1ProjectsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_sla_target_error_component import (
            ApiV1ProjectsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_slo_availability_error_component import (
            ApiV1ProjectsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_slo_target_error_component import (
            ApiV1ProjectsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_start_date_error_component import (
            ApiV1ProjectsCreateStartDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_target_availability_error_component import (
            ApiV1ProjectsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_tolerations_error_component import (
            ApiV1ProjectsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_projects_create_urls_error_component import (
            ApiV1ProjectsCreateUrlsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProjectsCreateActiveErrorComponent
                | ApiV1ProjectsCreateAnnotationsErrorComponent
                | ApiV1ProjectsCreateArchivedAtErrorComponent
                | ApiV1ProjectsCreateArchivedErrorComponent
                | ApiV1ProjectsCreateArchivedReasonErrorComponent
                | ApiV1ProjectsCreateBudgetedHoursErrorComponent
                | ApiV1ProjectsCreateBudgetedHoursIntervalErrorComponent
                | ApiV1ProjectsCreateBudgetedHoursModeErrorComponent
                | ApiV1ProjectsCreateCriticalityErrorComponent
                | ApiV1ProjectsCreateDebugModeErrorComponent
                | ApiV1ProjectsCreateDisplayNameErrorComponent
                | ApiV1ProjectsCreateEndDateErrorComponent
                | ApiV1ProjectsCreateKindErrorComponent
                | ApiV1ProjectsCreateLabelsErrorComponent
                | ApiV1ProjectsCreateNameErrorComponent
                | ApiV1ProjectsCreateNonFieldErrorsErrorComponent
                | ApiV1ProjectsCreateOrganizationIdErrorComponent
                | ApiV1ProjectsCreatePlatformServiceErrorComponent
                | ApiV1ProjectsCreateProductIdErrorComponent
                | ApiV1ProjectsCreateProviderErrorComponent
                | ApiV1ProjectsCreateProviderIdErrorComponent
                | ApiV1ProjectsCreateProviderReferenceErrorComponent
                | ApiV1ProjectsCreateReconciliationEnabledErrorComponent
                | ApiV1ProjectsCreateSlaAvailabilityErrorComponent
                | ApiV1ProjectsCreateSlaTargetErrorComponent
                | ApiV1ProjectsCreateSloAvailabilityErrorComponent
                | ApiV1ProjectsCreateSloTargetErrorComponent
                | ApiV1ProjectsCreateStartDateErrorComponent
                | ApiV1ProjectsCreateTargetAvailabilityErrorComponent
                | ApiV1ProjectsCreateTolerationsErrorComponent
                | ApiV1ProjectsCreateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_0 = (
                        ApiV1ProjectsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_1 = (
                        ApiV1ProjectsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_2 = (
                        ApiV1ProjectsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_3 = (
                        ApiV1ProjectsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_4 = (
                        ApiV1ProjectsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_5 = (
                        ApiV1ProjectsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_6 = (
                        ApiV1ProjectsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_7 = (
                        ApiV1ProjectsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_8 = (
                        ApiV1ProjectsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_9 = (
                        ApiV1ProjectsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_10 = (
                        ApiV1ProjectsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_11 = (
                        ApiV1ProjectsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_12 = (
                        ApiV1ProjectsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_13 = (
                        ApiV1ProjectsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_14 = (
                        ApiV1ProjectsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_15 = (
                        ApiV1ProjectsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_16 = (
                        ApiV1ProjectsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_17 = (
                        ApiV1ProjectsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_18 = (
                        ApiV1ProjectsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_19 = (
                        ApiV1ProjectsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_20 = (
                        ApiV1ProjectsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_21 = (
                        ApiV1ProjectsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_22 = (
                        ApiV1ProjectsCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_23 = (
                        ApiV1ProjectsCreateStartDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_24 = (
                        ApiV1ProjectsCreateEndDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_25 = (
                        ApiV1ProjectsCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_26 = (
                        ApiV1ProjectsCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_27 = (
                        ApiV1ProjectsCreateProductIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_28 = (
                        ApiV1ProjectsCreateBudgetedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_projects_create_error_type_29 = (
                        ApiV1ProjectsCreateBudgetedHoursIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_projects_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_projects_create_error_type_30 = (
                    ApiV1ProjectsCreateBudgetedHoursModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_projects_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_projects_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_projects_create_validation_error.additional_properties = d
        return api_v1_projects_create_validation_error

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
