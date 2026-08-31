from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pops_reconcile_create_annotations_error_component import (
        ApiV1PopsReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_archived_at_error_component import (
        ApiV1PopsReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_archived_error_component import (
        ApiV1PopsReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_archived_reason_error_component import (
        ApiV1PopsReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_city_error_component import ApiV1PopsReconcileCreateCityErrorComponent
    from ..models.api_v1_pops_reconcile_create_country_error_component import (
        ApiV1PopsReconcileCreateCountryErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_criticality_error_component import (
        ApiV1PopsReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_debug_mode_error_component import (
        ApiV1PopsReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_description_error_component import (
        ApiV1PopsReconcileCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_display_name_error_component import (
        ApiV1PopsReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_kind_error_component import ApiV1PopsReconcileCreateKindErrorComponent
    from ..models.api_v1_pops_reconcile_create_labels_error_component import (
        ApiV1PopsReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_latitude_error_component import (
        ApiV1PopsReconcileCreateLatitudeErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_longitude_error_component import (
        ApiV1PopsReconcileCreateLongitudeErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_name_error_component import ApiV1PopsReconcileCreateNameErrorComponent
    from ..models.api_v1_pops_reconcile_create_non_field_errors_error_component import (
        ApiV1PopsReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_platform_service_error_component import (
        ApiV1PopsReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_pop_endpoint_remote_address_error_component import (
        ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_provider_entity_id_error_component import (
        ApiV1PopsReconcileCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_provider_error_component import (
        ApiV1PopsReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_provider_id_error_component import (
        ApiV1PopsReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_provider_reference_error_component import (
        ApiV1PopsReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1PopsReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_region_error_component import (
        ApiV1PopsReconcileCreateRegionErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_sla_availability_error_component import (
        ApiV1PopsReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_sla_target_error_component import (
        ApiV1PopsReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_slo_availability_error_component import (
        ApiV1PopsReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_slo_target_error_component import (
        ApiV1PopsReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_target_availability_error_component import (
        ApiV1PopsReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_reconcile_create_tolerations_error_component import (
        ApiV1PopsReconcileCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PopsReconcileCreateValidationError")


@_attrs_define
class ApiV1PopsReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PopsReconcileCreateAnnotationsErrorComponent |
            ApiV1PopsReconcileCreateArchivedAtErrorComponent | ApiV1PopsReconcileCreateArchivedErrorComponent |
            ApiV1PopsReconcileCreateArchivedReasonErrorComponent | ApiV1PopsReconcileCreateCityErrorComponent |
            ApiV1PopsReconcileCreateCountryErrorComponent | ApiV1PopsReconcileCreateCriticalityErrorComponent |
            ApiV1PopsReconcileCreateDebugModeErrorComponent | ApiV1PopsReconcileCreateDescriptionErrorComponent |
            ApiV1PopsReconcileCreateDisplayNameErrorComponent | ApiV1PopsReconcileCreateKindErrorComponent |
            ApiV1PopsReconcileCreateLabelsErrorComponent | ApiV1PopsReconcileCreateLatitudeErrorComponent |
            ApiV1PopsReconcileCreateLongitudeErrorComponent | ApiV1PopsReconcileCreateNameErrorComponent |
            ApiV1PopsReconcileCreateNonFieldErrorsErrorComponent | ApiV1PopsReconcileCreatePlatformServiceErrorComponent |
            ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponent |
            ApiV1PopsReconcileCreateProviderEntityIdErrorComponent | ApiV1PopsReconcileCreateProviderErrorComponent |
            ApiV1PopsReconcileCreateProviderIdErrorComponent | ApiV1PopsReconcileCreateProviderReferenceErrorComponent |
            ApiV1PopsReconcileCreateReconciliationEnabledErrorComponent | ApiV1PopsReconcileCreateRegionErrorComponent |
            ApiV1PopsReconcileCreateSlaAvailabilityErrorComponent | ApiV1PopsReconcileCreateSlaTargetErrorComponent |
            ApiV1PopsReconcileCreateSloAvailabilityErrorComponent | ApiV1PopsReconcileCreateSloTargetErrorComponent |
            ApiV1PopsReconcileCreateTargetAvailabilityErrorComponent | ApiV1PopsReconcileCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PopsReconcileCreateAnnotationsErrorComponent
        | ApiV1PopsReconcileCreateArchivedAtErrorComponent
        | ApiV1PopsReconcileCreateArchivedErrorComponent
        | ApiV1PopsReconcileCreateArchivedReasonErrorComponent
        | ApiV1PopsReconcileCreateCityErrorComponent
        | ApiV1PopsReconcileCreateCountryErrorComponent
        | ApiV1PopsReconcileCreateCriticalityErrorComponent
        | ApiV1PopsReconcileCreateDebugModeErrorComponent
        | ApiV1PopsReconcileCreateDescriptionErrorComponent
        | ApiV1PopsReconcileCreateDisplayNameErrorComponent
        | ApiV1PopsReconcileCreateKindErrorComponent
        | ApiV1PopsReconcileCreateLabelsErrorComponent
        | ApiV1PopsReconcileCreateLatitudeErrorComponent
        | ApiV1PopsReconcileCreateLongitudeErrorComponent
        | ApiV1PopsReconcileCreateNameErrorComponent
        | ApiV1PopsReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1PopsReconcileCreatePlatformServiceErrorComponent
        | ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponent
        | ApiV1PopsReconcileCreateProviderEntityIdErrorComponent
        | ApiV1PopsReconcileCreateProviderErrorComponent
        | ApiV1PopsReconcileCreateProviderIdErrorComponent
        | ApiV1PopsReconcileCreateProviderReferenceErrorComponent
        | ApiV1PopsReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1PopsReconcileCreateRegionErrorComponent
        | ApiV1PopsReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1PopsReconcileCreateSlaTargetErrorComponent
        | ApiV1PopsReconcileCreateSloAvailabilityErrorComponent
        | ApiV1PopsReconcileCreateSloTargetErrorComponent
        | ApiV1PopsReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1PopsReconcileCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pops_reconcile_create_annotations_error_component import (
            ApiV1PopsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_archived_at_error_component import (
            ApiV1PopsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_archived_error_component import (
            ApiV1PopsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_archived_reason_error_component import (
            ApiV1PopsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_city_error_component import (
            ApiV1PopsReconcileCreateCityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_country_error_component import (
            ApiV1PopsReconcileCreateCountryErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_criticality_error_component import (
            ApiV1PopsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_debug_mode_error_component import (
            ApiV1PopsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_description_error_component import (
            ApiV1PopsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_display_name_error_component import (
            ApiV1PopsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_kind_error_component import (
            ApiV1PopsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_labels_error_component import (
            ApiV1PopsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_latitude_error_component import (
            ApiV1PopsReconcileCreateLatitudeErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_longitude_error_component import (
            ApiV1PopsReconcileCreateLongitudeErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_name_error_component import (
            ApiV1PopsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_non_field_errors_error_component import (
            ApiV1PopsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_platform_service_error_component import (
            ApiV1PopsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_provider_entity_id_error_component import (
            ApiV1PopsReconcileCreateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_provider_error_component import (
            ApiV1PopsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_provider_id_error_component import (
            ApiV1PopsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_provider_reference_error_component import (
            ApiV1PopsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1PopsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_region_error_component import (
            ApiV1PopsReconcileCreateRegionErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_sla_availability_error_component import (
            ApiV1PopsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_sla_target_error_component import (
            ApiV1PopsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_slo_availability_error_component import (
            ApiV1PopsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_slo_target_error_component import (
            ApiV1PopsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_target_availability_error_component import (
            ApiV1PopsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_tolerations_error_component import (
            ApiV1PopsReconcileCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PopsReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateLatitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateLongitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsReconcileCreateProviderEntityIdErrorComponent):
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
        from ..models.api_v1_pops_reconcile_create_annotations_error_component import (
            ApiV1PopsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_archived_at_error_component import (
            ApiV1PopsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_archived_error_component import (
            ApiV1PopsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_archived_reason_error_component import (
            ApiV1PopsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_city_error_component import (
            ApiV1PopsReconcileCreateCityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_country_error_component import (
            ApiV1PopsReconcileCreateCountryErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_criticality_error_component import (
            ApiV1PopsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_debug_mode_error_component import (
            ApiV1PopsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_description_error_component import (
            ApiV1PopsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_display_name_error_component import (
            ApiV1PopsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_kind_error_component import (
            ApiV1PopsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_labels_error_component import (
            ApiV1PopsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_latitude_error_component import (
            ApiV1PopsReconcileCreateLatitudeErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_longitude_error_component import (
            ApiV1PopsReconcileCreateLongitudeErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_name_error_component import (
            ApiV1PopsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_non_field_errors_error_component import (
            ApiV1PopsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_platform_service_error_component import (
            ApiV1PopsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_pop_endpoint_remote_address_error_component import (
            ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_provider_entity_id_error_component import (
            ApiV1PopsReconcileCreateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_provider_error_component import (
            ApiV1PopsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_provider_id_error_component import (
            ApiV1PopsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_provider_reference_error_component import (
            ApiV1PopsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1PopsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_region_error_component import (
            ApiV1PopsReconcileCreateRegionErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_sla_availability_error_component import (
            ApiV1PopsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_sla_target_error_component import (
            ApiV1PopsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_slo_availability_error_component import (
            ApiV1PopsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_slo_target_error_component import (
            ApiV1PopsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_target_availability_error_component import (
            ApiV1PopsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_reconcile_create_tolerations_error_component import (
            ApiV1PopsReconcileCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PopsReconcileCreateAnnotationsErrorComponent
                | ApiV1PopsReconcileCreateArchivedAtErrorComponent
                | ApiV1PopsReconcileCreateArchivedErrorComponent
                | ApiV1PopsReconcileCreateArchivedReasonErrorComponent
                | ApiV1PopsReconcileCreateCityErrorComponent
                | ApiV1PopsReconcileCreateCountryErrorComponent
                | ApiV1PopsReconcileCreateCriticalityErrorComponent
                | ApiV1PopsReconcileCreateDebugModeErrorComponent
                | ApiV1PopsReconcileCreateDescriptionErrorComponent
                | ApiV1PopsReconcileCreateDisplayNameErrorComponent
                | ApiV1PopsReconcileCreateKindErrorComponent
                | ApiV1PopsReconcileCreateLabelsErrorComponent
                | ApiV1PopsReconcileCreateLatitudeErrorComponent
                | ApiV1PopsReconcileCreateLongitudeErrorComponent
                | ApiV1PopsReconcileCreateNameErrorComponent
                | ApiV1PopsReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1PopsReconcileCreatePlatformServiceErrorComponent
                | ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponent
                | ApiV1PopsReconcileCreateProviderEntityIdErrorComponent
                | ApiV1PopsReconcileCreateProviderErrorComponent
                | ApiV1PopsReconcileCreateProviderIdErrorComponent
                | ApiV1PopsReconcileCreateProviderReferenceErrorComponent
                | ApiV1PopsReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1PopsReconcileCreateRegionErrorComponent
                | ApiV1PopsReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1PopsReconcileCreateSlaTargetErrorComponent
                | ApiV1PopsReconcileCreateSloAvailabilityErrorComponent
                | ApiV1PopsReconcileCreateSloTargetErrorComponent
                | ApiV1PopsReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1PopsReconcileCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_0 = (
                        ApiV1PopsReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_1 = (
                        ApiV1PopsReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_2 = (
                        ApiV1PopsReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_3 = (
                        ApiV1PopsReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_4 = (
                        ApiV1PopsReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_5 = (
                        ApiV1PopsReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_6 = (
                        ApiV1PopsReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_7 = (
                        ApiV1PopsReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_8 = (
                        ApiV1PopsReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_9 = (
                        ApiV1PopsReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_10 = (
                        ApiV1PopsReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_11 = (
                        ApiV1PopsReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_12 = (
                        ApiV1PopsReconcileCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_13 = (
                        ApiV1PopsReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_14 = (
                        ApiV1PopsReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_15 = (
                        ApiV1PopsReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_16 = (
                        ApiV1PopsReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_17 = (
                        ApiV1PopsReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_18 = (
                        ApiV1PopsReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_19 = (
                        ApiV1PopsReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_20 = (
                        ApiV1PopsReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_21 = (
                        ApiV1PopsReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_22 = (
                        ApiV1PopsReconcileCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_23 = (
                        ApiV1PopsReconcileCreateCountryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_24 = (
                        ApiV1PopsReconcileCreateCityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_25 = (
                        ApiV1PopsReconcileCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_26 = (
                        ApiV1PopsReconcileCreateLatitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_27 = (
                        ApiV1PopsReconcileCreateLongitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_reconcile_create_error_type_28 = (
                        ApiV1PopsReconcileCreateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pops_reconcile_create_error_type_29 = (
                    ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pops_reconcile_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pops_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pops_reconcile_create_validation_error.additional_properties = d
        return api_v1_pops_reconcile_create_validation_error

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
