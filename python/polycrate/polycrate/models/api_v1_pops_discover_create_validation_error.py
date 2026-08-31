from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pops_discover_create_annotations_error_component import (
        ApiV1PopsDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_archived_at_error_component import (
        ApiV1PopsDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_archived_error_component import (
        ApiV1PopsDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_archived_reason_error_component import (
        ApiV1PopsDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_city_error_component import ApiV1PopsDiscoverCreateCityErrorComponent
    from ..models.api_v1_pops_discover_create_country_error_component import (
        ApiV1PopsDiscoverCreateCountryErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_criticality_error_component import (
        ApiV1PopsDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_debug_mode_error_component import (
        ApiV1PopsDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_description_error_component import (
        ApiV1PopsDiscoverCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_display_name_error_component import (
        ApiV1PopsDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_kind_error_component import ApiV1PopsDiscoverCreateKindErrorComponent
    from ..models.api_v1_pops_discover_create_labels_error_component import ApiV1PopsDiscoverCreateLabelsErrorComponent
    from ..models.api_v1_pops_discover_create_latitude_error_component import (
        ApiV1PopsDiscoverCreateLatitudeErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_longitude_error_component import (
        ApiV1PopsDiscoverCreateLongitudeErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_name_error_component import ApiV1PopsDiscoverCreateNameErrorComponent
    from ..models.api_v1_pops_discover_create_non_field_errors_error_component import (
        ApiV1PopsDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_platform_service_error_component import (
        ApiV1PopsDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_pop_endpoint_remote_address_error_component import (
        ApiV1PopsDiscoverCreatePopEndpointRemoteAddressErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_provider_entity_id_error_component import (
        ApiV1PopsDiscoverCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_provider_error_component import (
        ApiV1PopsDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_provider_id_error_component import (
        ApiV1PopsDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_provider_reference_error_component import (
        ApiV1PopsDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_reconciliation_enabled_error_component import (
        ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_region_error_component import ApiV1PopsDiscoverCreateRegionErrorComponent
    from ..models.api_v1_pops_discover_create_sla_availability_error_component import (
        ApiV1PopsDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_sla_target_error_component import (
        ApiV1PopsDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_slo_availability_error_component import (
        ApiV1PopsDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_slo_target_error_component import (
        ApiV1PopsDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_target_availability_error_component import (
        ApiV1PopsDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_discover_create_tolerations_error_component import (
        ApiV1PopsDiscoverCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PopsDiscoverCreateValidationError")


@_attrs_define
class ApiV1PopsDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PopsDiscoverCreateAnnotationsErrorComponent | ApiV1PopsDiscoverCreateArchivedAtErrorComponent
            | ApiV1PopsDiscoverCreateArchivedErrorComponent | ApiV1PopsDiscoverCreateArchivedReasonErrorComponent |
            ApiV1PopsDiscoverCreateCityErrorComponent | ApiV1PopsDiscoverCreateCountryErrorComponent |
            ApiV1PopsDiscoverCreateCriticalityErrorComponent | ApiV1PopsDiscoverCreateDebugModeErrorComponent |
            ApiV1PopsDiscoverCreateDescriptionErrorComponent | ApiV1PopsDiscoverCreateDisplayNameErrorComponent |
            ApiV1PopsDiscoverCreateKindErrorComponent | ApiV1PopsDiscoverCreateLabelsErrorComponent |
            ApiV1PopsDiscoverCreateLatitudeErrorComponent | ApiV1PopsDiscoverCreateLongitudeErrorComponent |
            ApiV1PopsDiscoverCreateNameErrorComponent | ApiV1PopsDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1PopsDiscoverCreatePlatformServiceErrorComponent |
            ApiV1PopsDiscoverCreatePopEndpointRemoteAddressErrorComponent |
            ApiV1PopsDiscoverCreateProviderEntityIdErrorComponent | ApiV1PopsDiscoverCreateProviderErrorComponent |
            ApiV1PopsDiscoverCreateProviderIdErrorComponent | ApiV1PopsDiscoverCreateProviderReferenceErrorComponent |
            ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponent | ApiV1PopsDiscoverCreateRegionErrorComponent |
            ApiV1PopsDiscoverCreateSlaAvailabilityErrorComponent | ApiV1PopsDiscoverCreateSlaTargetErrorComponent |
            ApiV1PopsDiscoverCreateSloAvailabilityErrorComponent | ApiV1PopsDiscoverCreateSloTargetErrorComponent |
            ApiV1PopsDiscoverCreateTargetAvailabilityErrorComponent | ApiV1PopsDiscoverCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PopsDiscoverCreateAnnotationsErrorComponent
        | ApiV1PopsDiscoverCreateArchivedAtErrorComponent
        | ApiV1PopsDiscoverCreateArchivedErrorComponent
        | ApiV1PopsDiscoverCreateArchivedReasonErrorComponent
        | ApiV1PopsDiscoverCreateCityErrorComponent
        | ApiV1PopsDiscoverCreateCountryErrorComponent
        | ApiV1PopsDiscoverCreateCriticalityErrorComponent
        | ApiV1PopsDiscoverCreateDebugModeErrorComponent
        | ApiV1PopsDiscoverCreateDescriptionErrorComponent
        | ApiV1PopsDiscoverCreateDisplayNameErrorComponent
        | ApiV1PopsDiscoverCreateKindErrorComponent
        | ApiV1PopsDiscoverCreateLabelsErrorComponent
        | ApiV1PopsDiscoverCreateLatitudeErrorComponent
        | ApiV1PopsDiscoverCreateLongitudeErrorComponent
        | ApiV1PopsDiscoverCreateNameErrorComponent
        | ApiV1PopsDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1PopsDiscoverCreatePlatformServiceErrorComponent
        | ApiV1PopsDiscoverCreatePopEndpointRemoteAddressErrorComponent
        | ApiV1PopsDiscoverCreateProviderEntityIdErrorComponent
        | ApiV1PopsDiscoverCreateProviderErrorComponent
        | ApiV1PopsDiscoverCreateProviderIdErrorComponent
        | ApiV1PopsDiscoverCreateProviderReferenceErrorComponent
        | ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1PopsDiscoverCreateRegionErrorComponent
        | ApiV1PopsDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1PopsDiscoverCreateSlaTargetErrorComponent
        | ApiV1PopsDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1PopsDiscoverCreateSloTargetErrorComponent
        | ApiV1PopsDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1PopsDiscoverCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pops_discover_create_annotations_error_component import (
            ApiV1PopsDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_archived_at_error_component import (
            ApiV1PopsDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_archived_error_component import (
            ApiV1PopsDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_archived_reason_error_component import (
            ApiV1PopsDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_city_error_component import ApiV1PopsDiscoverCreateCityErrorComponent
        from ..models.api_v1_pops_discover_create_country_error_component import (
            ApiV1PopsDiscoverCreateCountryErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_criticality_error_component import (
            ApiV1PopsDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_debug_mode_error_component import (
            ApiV1PopsDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_description_error_component import (
            ApiV1PopsDiscoverCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_display_name_error_component import (
            ApiV1PopsDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_kind_error_component import ApiV1PopsDiscoverCreateKindErrorComponent
        from ..models.api_v1_pops_discover_create_labels_error_component import (
            ApiV1PopsDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_latitude_error_component import (
            ApiV1PopsDiscoverCreateLatitudeErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_longitude_error_component import (
            ApiV1PopsDiscoverCreateLongitudeErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_name_error_component import ApiV1PopsDiscoverCreateNameErrorComponent
        from ..models.api_v1_pops_discover_create_non_field_errors_error_component import (
            ApiV1PopsDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_platform_service_error_component import (
            ApiV1PopsDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_provider_entity_id_error_component import (
            ApiV1PopsDiscoverCreateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_provider_error_component import (
            ApiV1PopsDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_provider_id_error_component import (
            ApiV1PopsDiscoverCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_provider_reference_error_component import (
            ApiV1PopsDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_reconciliation_enabled_error_component import (
            ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_region_error_component import (
            ApiV1PopsDiscoverCreateRegionErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_sla_availability_error_component import (
            ApiV1PopsDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_sla_target_error_component import (
            ApiV1PopsDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_slo_availability_error_component import (
            ApiV1PopsDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_slo_target_error_component import (
            ApiV1PopsDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_target_availability_error_component import (
            ApiV1PopsDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_tolerations_error_component import (
            ApiV1PopsDiscoverCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PopsDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateLatitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateLongitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsDiscoverCreateProviderEntityIdErrorComponent):
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
        from ..models.api_v1_pops_discover_create_annotations_error_component import (
            ApiV1PopsDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_archived_at_error_component import (
            ApiV1PopsDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_archived_error_component import (
            ApiV1PopsDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_archived_reason_error_component import (
            ApiV1PopsDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_city_error_component import ApiV1PopsDiscoverCreateCityErrorComponent
        from ..models.api_v1_pops_discover_create_country_error_component import (
            ApiV1PopsDiscoverCreateCountryErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_criticality_error_component import (
            ApiV1PopsDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_debug_mode_error_component import (
            ApiV1PopsDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_description_error_component import (
            ApiV1PopsDiscoverCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_display_name_error_component import (
            ApiV1PopsDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_kind_error_component import ApiV1PopsDiscoverCreateKindErrorComponent
        from ..models.api_v1_pops_discover_create_labels_error_component import (
            ApiV1PopsDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_latitude_error_component import (
            ApiV1PopsDiscoverCreateLatitudeErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_longitude_error_component import (
            ApiV1PopsDiscoverCreateLongitudeErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_name_error_component import ApiV1PopsDiscoverCreateNameErrorComponent
        from ..models.api_v1_pops_discover_create_non_field_errors_error_component import (
            ApiV1PopsDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_platform_service_error_component import (
            ApiV1PopsDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_pop_endpoint_remote_address_error_component import (
            ApiV1PopsDiscoverCreatePopEndpointRemoteAddressErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_provider_entity_id_error_component import (
            ApiV1PopsDiscoverCreateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_provider_error_component import (
            ApiV1PopsDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_provider_id_error_component import (
            ApiV1PopsDiscoverCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_provider_reference_error_component import (
            ApiV1PopsDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_reconciliation_enabled_error_component import (
            ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_region_error_component import (
            ApiV1PopsDiscoverCreateRegionErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_sla_availability_error_component import (
            ApiV1PopsDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_sla_target_error_component import (
            ApiV1PopsDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_slo_availability_error_component import (
            ApiV1PopsDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_slo_target_error_component import (
            ApiV1PopsDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_target_availability_error_component import (
            ApiV1PopsDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_discover_create_tolerations_error_component import (
            ApiV1PopsDiscoverCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PopsDiscoverCreateAnnotationsErrorComponent
                | ApiV1PopsDiscoverCreateArchivedAtErrorComponent
                | ApiV1PopsDiscoverCreateArchivedErrorComponent
                | ApiV1PopsDiscoverCreateArchivedReasonErrorComponent
                | ApiV1PopsDiscoverCreateCityErrorComponent
                | ApiV1PopsDiscoverCreateCountryErrorComponent
                | ApiV1PopsDiscoverCreateCriticalityErrorComponent
                | ApiV1PopsDiscoverCreateDebugModeErrorComponent
                | ApiV1PopsDiscoverCreateDescriptionErrorComponent
                | ApiV1PopsDiscoverCreateDisplayNameErrorComponent
                | ApiV1PopsDiscoverCreateKindErrorComponent
                | ApiV1PopsDiscoverCreateLabelsErrorComponent
                | ApiV1PopsDiscoverCreateLatitudeErrorComponent
                | ApiV1PopsDiscoverCreateLongitudeErrorComponent
                | ApiV1PopsDiscoverCreateNameErrorComponent
                | ApiV1PopsDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1PopsDiscoverCreatePlatformServiceErrorComponent
                | ApiV1PopsDiscoverCreatePopEndpointRemoteAddressErrorComponent
                | ApiV1PopsDiscoverCreateProviderEntityIdErrorComponent
                | ApiV1PopsDiscoverCreateProviderErrorComponent
                | ApiV1PopsDiscoverCreateProviderIdErrorComponent
                | ApiV1PopsDiscoverCreateProviderReferenceErrorComponent
                | ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1PopsDiscoverCreateRegionErrorComponent
                | ApiV1PopsDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1PopsDiscoverCreateSlaTargetErrorComponent
                | ApiV1PopsDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1PopsDiscoverCreateSloTargetErrorComponent
                | ApiV1PopsDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1PopsDiscoverCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_0 = (
                        ApiV1PopsDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_1 = (
                        ApiV1PopsDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_2 = (
                        ApiV1PopsDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_3 = (
                        ApiV1PopsDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_4 = (
                        ApiV1PopsDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_5 = (
                        ApiV1PopsDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_6 = (
                        ApiV1PopsDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_7 = (
                        ApiV1PopsDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_8 = (
                        ApiV1PopsDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_9 = (
                        ApiV1PopsDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_10 = (
                        ApiV1PopsDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_11 = (
                        ApiV1PopsDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_12 = (
                        ApiV1PopsDiscoverCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_13 = (
                        ApiV1PopsDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_14 = (
                        ApiV1PopsDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_15 = (
                        ApiV1PopsDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_16 = (
                        ApiV1PopsDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_17 = (
                        ApiV1PopsDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_18 = (
                        ApiV1PopsDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_19 = (
                        ApiV1PopsDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_20 = (
                        ApiV1PopsDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_21 = (
                        ApiV1PopsDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_22 = (
                        ApiV1PopsDiscoverCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_23 = (
                        ApiV1PopsDiscoverCreateCountryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_24 = (
                        ApiV1PopsDiscoverCreateCityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_25 = (
                        ApiV1PopsDiscoverCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_26 = (
                        ApiV1PopsDiscoverCreateLatitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_27 = (
                        ApiV1PopsDiscoverCreateLongitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_discover_create_error_type_28 = (
                        ApiV1PopsDiscoverCreateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pops_discover_create_error_type_29 = (
                    ApiV1PopsDiscoverCreatePopEndpointRemoteAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pops_discover_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pops_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pops_discover_create_validation_error.additional_properties = d
        return api_v1_pops_discover_create_validation_error

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
